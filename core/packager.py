# core/packager.py

import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger(__name__)


def clean_temp_files(serverpack_path: Path, extra_exclude: list[str] = None):
    """
    Removes unneeded files before packaging (e.g., logs, installers).
    """
    logger.info("Cleaning up temporary and unnecessary files...")
    exclude = [".log", ".jar", ".tmp", "installer.jar"]
    if extra_exclude:
        exclude.extend(extra_exclude)

    for file in serverpack_path.glob("**/*"):
        if file.is_file() and any(str(file.name).endswith(ext) for ext in exclude):
            logger.debug(f"Removing: {file}")
            file.unlink()


def generate_readme(template: str, output_path: Path, context: dict):
    """
    Generates a README.md file from a template using context variables.
    """
    readme_content = template.format(**context)
    readme_path = output_path / "README.md"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    logger.info(f"README.md generated at {readme_path}")


def zip_server_pack(serverpack_dir: Path, output_dir: Path, name_template: str, context: dict) -> Path:
    """
    Zips the server pack directory into a .zip archive.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Replace placeholders in zip name
    zip_name = name_template.format(
        modpack_name=context.get("modpack_name", "modpack"),
        mc_version=context.get("mc_version", "unknown"),
        modloader=context.get("modloader", "forge"),
        modloader_version=context.get("modloader_version", "latest"),
        date=datetime.now().strftime("%Y%m%d")
    )

    zip_path = output_dir / f"{zip_name}.zip"
    logger.info(f"Creating ZIP archive at: {zip_path}")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in serverpack_dir.rglob("*"):
            if file.is_file():
                zipf.write(file, arcname=file.relative_to(serverpack_dir))
                logger.debug(f"Added to zip: {file.relative_to(serverpack_dir)}")

    logger.success(f"Server pack zipped at: {zip_path}")
    return zip_path
