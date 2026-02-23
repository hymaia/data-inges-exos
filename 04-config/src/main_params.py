import argparse


def run(db_host: str, db_port: int, api_key: str):
    print(f"Connexion à {db_host}:{db_port}")
    print(f"Clé API : {api_key}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hello app")
    parser.add_argument("--db-host", required=True, help="Database host")
    parser.add_argument("--db-port", type=int, default=5432, help="Database port")
    parser.add_argument("--api-key", required=True, help="API key")

    args = parser.parse_args()

    run(
        db_host=args.db_host,
        db_port=args.db_port,
        api_key=args.api_key,
    )
