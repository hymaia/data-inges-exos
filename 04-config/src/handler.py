import json
import os
import boto3


def handler(event, context):
    region = os.environ.get("AWS_REGION", "eu-west-1")
    env = os.environ.get("ENVIRONMENT", "local")
    param_path = os.environ["PARAM_PATH"]
    secret_name = os.environ["SECRET_PATH"]

    ssm = boto3.client("ssm", region_name=region)
    secretsmanager = boto3.client("secretsmanager", region_name=region)

    param_response = ssm.get_parameter(Name=param_path, WithDecryption=False)
    param_value = param_response["Parameter"]["Value"]

    secret_response = secretsmanager.get_secret_value(SecretId=secret_name)
    secret_value = (
        json.loads(secret_response["SecretString"])
        if "SecretString" in secret_response
        else secret_response["SecretBinary"].decode("utf-8")
    )

    print(f"[PARAM]  {param_path} = {param_value}")
    print(f"[SECRET] {secret_name} = {secret_value}")
    print(f"[ENV] env = {env}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "param": {
                "path": param_path,
                "value": param_value,
            },
            "secret": {
                "name": secret_name,
                "value": secret_value,
            },
        }),
    }
