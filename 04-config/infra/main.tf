terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# ──────────────────────────────────────────────
# Variables
# ──────────────────────────────────────────────

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "hello"
}

# ──────────────────────────────────────────────
# Secret
# ──────────────────────────────────────────────

resource "aws_secretsmanager_secret" "api_key" {
  name = "/${var.environment}/${var.app_name}/api_key"

  tags = {
    Environment = var.environment
    App         = var.app_name
    ManagedBy   = "terraform"
  }
}

# ──────────────────────────────────────────────
# SSM – Non-secret parameter (String)
# ──────────────────────────────────────────────

resource "aws_ssm_parameter" "db_host" {
  name        = "/${var.environment}/${var.app_name}/config/param"
  description = "Non-secret parameter for ${var.app_name}"
  type        = "String"
  value       = "localhost"

  tags = {
    Environment = var.environment
    App         = var.app_name
    ManagedBy   = "terraform"
  }
}

resource "aws_ssm_parameter" "db_port" {
  name        = "/${var.environment}/${var.app_name}/config/param"
  description = "Non-secret parameter for ${var.app_name}"
  type        = "String"
  value       = "5432"

  tags = {
    Environment = var.environment
    App         = var.app_name
    ManagedBy   = "terraform"
  }
}

# ──────────────────────────────────────────────
# IAM – Role & policies for Lambda
# ──────────────────────────────────────────────

data "aws_iam_policy_document" "lambda_assume_role" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "lambda" {
  name               = "${var.environment}-${var.app_name}-lambda-role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role.json

  tags = {
    Environment = var.environment
    App         = var.app_name
    ManagedBy   = "terraform"
  }
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

data "aws_iam_policy_document" "lambda_ssm" {
  statement {
    effect = "Allow"
    actions = [
      "ssm:GetParameter",
      "ssm:GetParameters",
      "ssm:GetParametersByPath",
    ]
    resources = [
      aws_ssm_parameter.db_host.arn,
      aws_ssm_parameter.db_port.arn,
    ]
  }
  statement {
    effect = "Allow"
    actions = [
      "secretsmanager:GetSecretValue",
      "secretsmanager:DescribeSecret",
    ]
    resources = [
      aws_secretsmanager_secret.api_key.arn,
    ]
  }
  statement {
    effect = "Allow"
    actions = [
      "secretsmanager:ListSecrets",
    ]
    resources = [
      "*",
    ]
  }

  statement {
    effect    = "Allow"
    actions   = ["kms:Decrypt"]
    resources = ["*"]
  }
}

resource "aws_iam_role_policy" "lambda_ssm" {
  name   = "${var.environment}-${var.app_name}-ssm-policy"
  role   = aws_iam_role.lambda.id
  policy = data.aws_iam_policy_document.lambda_ssm.json
}

# ──────────────────────────────────────────────
# Lambda – package & function
# ──────────────────────────────────────────────

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../src/handler.py"
  output_path = "${path.module}/../src/handler.zip"
}

resource "aws_lambda_function" "hello" {
  function_name    = "${var.environment}-${var.app_name}"
  description      = "Hello Lambda – ${var.environment}"
  role             = aws_iam_role.lambda.arn
  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  handler          = "handler.handler"
  runtime          = "python3.12"
  timeout          = 30
  memory_size      = 128

  environment {
    variables = {
      ENVIRONMENT         = var.environment
      API_KEY_SECRET_NAME = aws_secretsmanager_secret.api_key.name
      DB_HOST_PARAM_NAME  = aws_ssm_parameter.db_host.name
      DB_PORT_PARAM_NAME  = aws_ssm_parameter.db_port.name
    }
  }

  tags = {
    Environment = var.environment
    App         = var.app_name
    ManagedBy   = "terraform"
  }
}

# ──────────────────────────────────────────────
# CloudWatch – Log group
# ──────────────────────────────────────────────

resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${aws_lambda_function.hello.function_name}"
  retention_in_days = 1

  tags = {
    Environment = var.environment
    App         = var.app_name
    ManagedBy   = "terraform"
  }
}

# ──────────────────────────────────────────────
# Outputs
# ──────────────────────────────────────────────

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.hello.function_name
}

output "lambda_function_arn" {
  description = "ARN of the Lambda function"
  value       = aws_lambda_function.hello.arn
}
