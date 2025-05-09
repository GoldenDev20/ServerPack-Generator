# core/forge_installer.py

import requests
import shutil
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger(__name__)

FORGE_BASE_URL = "https://maven.minecraftforge.net/net/minecraftforge/forge"


def build_forge_url(mc_version: str, forge_version: str) -> str:
    """
    Constructs the full URL to the Forge universal installer JAR.
    """
    full_version = f"{mc_version}-{forge_version}"
    file_name = f"forge-{full_version}-installer.jar"
    return f"{FORGE_BASE_URL}/{full_version}/{file_name}", file_name


def download_forge_installer(mc_version: str, forge_version: str, output_dir: str | Path) -> Path | None:
    """
    Downloads the Forge installer JAR to the specified output directory.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    url, file_name = build_forge_url(mc_version, forge_version)
    output_path = output_dir / file_name

    logger.info(f"Attempting to download Forge installer from:\n{url}")
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            shutil.copyfileobj(response.raw, f)

        logger.info(f"Forge installer downloaded to: {output_path}")
        return output_path

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download Forge installer: {e}")
        return None
