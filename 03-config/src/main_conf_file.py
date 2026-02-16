import yaml
from pathlib import Path


def load_config(path: str = "config.yaml") -> dict:
    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable : {path}")

    with config_path.open() as f:
        return yaml.safe_load(f)


def run(config: dict):
    print(f"Connexion à {config['db_host']}:{config['db_port']}")
    print(f"Clé API : {config['api_key']}")


if __name__ == "__main__":
    config = load_config("config.yaml")
    run(config)
