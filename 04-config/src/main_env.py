import os
from dataclasses import dataclass


@dataclass
class Config:
    db_host: str
    db_port: int
    api_key: str


def load_config() -> Config:
    missing = [k for k in ["DB_HOST", "API_KEY"] if not os.environ.get(k)]
    if missing:
        raise EnvironmentError(f"Variables d'environnement manquantes : {missing}")

    return Config(
        db_host=os.environ["DB_HOST"],
        db_port=int(os.environ.get("DB_PORT", "5432")),
        api_key=os.environ["API_KEY"],
    )


def run(config: Config):
    print(f"Connexion à {config.db_host}:{config.db_port}")
    print(f"Clé API : {config.api_key}")


if __name__ == "__main__":
    config = load_config()
    run(config)
