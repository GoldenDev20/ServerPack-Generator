# core/file_manager.py

import os
import shutil
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger(__name__)

def ensure_directory(path: str | Path) -> None:
    """
    Ensures that a directory exists. Creates it if missing.
    """
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory: {path}")
    else:
        logger.debug(f"Directory already exists: {path}")


def clear_directory(path: str | Path) -> None:
    """
    Removes all contents of a directory, preserving the folder.
    """
    path = Path(path)
    if path.exists() and path.is_dir():
        for item in path.iterdir():
            if item.is_file() or item.is_symlink():
                item.unlink()
                logger.debug(f"Deleted file: {item}")
            elif item.is_dir():
                shutil.rmtree(item)
                logger.debug(f"Deleted directory: {item}")
        logger.info(f"Cleared contents of: {path}")
    else:
        logger.warning(f"Directory not found or not valid: {path}")


def copy_directory(source: str | Path, destination: str | Path, ignore_list: list[str] = None) -> None:
    """
    Recursively copies a directory from source to destination, excluding paths in ignore_list.
    """
    source = Path(source)
    destination = Path(destination)
    ignore_list = ignore_list or []

    if not source.exists():
        logger.warning(f"Source path does not exist: {source}")
        return

    if not source.is_dir():
        logger.error(f"Source is not a directory: {source}")
        return

    ensure_directory(destination)

    for item in source.iterdir():
        if item.name in ignore_list:
            logger.debug(f"Skipping excluded item: {item.name}")
            continue

        dest_path = destination / item.name
        if item.is_dir():
            shutil.copytree(item, dest_path, dirs_exist_ok=True)
            logger.info(f"Copied directory: {item} → {dest_path}")
        else:
            shutil.copy2(item, dest_path)
            logger.info(f"Copied file: {item} → {dest_path}")


def copy_file(source: str | Path, destination: str | Path) -> None:
    """
    Copies a single file from source to destination.
    """
    source = Path(source)
    destination = Path(destination)

    if not source.exists():
        logger.warning(f"File not found: {source}")
        return

    ensure_directory(destination.parent)
    shutil.copy2(source, destination)
    logger.info(f"Copied file: {source} → {destination}")
