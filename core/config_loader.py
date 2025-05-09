# core/config_loader.py

import yaml
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger(__name__)
CONFIG_PATH = Path("config.yaml")
TEMPLATE_PATH = Path("templates/default_config.yaml")


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        logger.warning("No config.yaml found. Creating from default template.")

        if not TEMPLATE_PATH.exists():
            logger.critical("Default template is missing. Aborting.")
            raise SystemExit("Error: default_config.yaml not found in templates/.")

        try:
            with open(TEMPLATE_PATH, "r") as f:
                default_config = yaml.safe_load(f)

            with open(CONFIG_PATH, "w") as f:
                yaml.dump(default_config, f, sort_keys=False)

            logger.info("Generated config.yaml from default template.")
            return default_config

        except yaml.YAMLError as e:
            logger.error(f"Error parsing template config: {e}")
            raise SystemExit("Error: Template config is invalid YAML.")

    # Load existing config
    try:
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)
        logger.info("Loaded configuration from config.yaml.")
        return config

    except yaml.YAMLError as e:
        logger.error(f"Failed to parse config.yaml: {e}")
        raise SystemExit("Error: Could not load configuration. Check YAML format.")

    except Exception as e:
        logger.error(f"Unexpected error loading config: {e}")
        raise SystemExit("Error: Unexpected configuration issue.")
