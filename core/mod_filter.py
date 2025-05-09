# core/mod_filter.py

import os
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger(__name__)

# Known client-only mod indicators (extendable)
DEFAULT_CLIENT_ONLY_PATTERNS = [
    "optifine", "oculus", "rubidium", "sodium",
    "iris", "journeymap", "screenshot", "lithium",
    "tweakeroo", "itemphysic", "firstperson", "replaymod",
    "smoothboot", "neat", "xaero", "betterfps", "fancymenu"
]

def is_client_mod(mod_filename: str, patterns: list[str]) -> bool:
    """
    Determines whether a mod is client-only based on known patterns.
    """
    lower_name = mod_filename.lower()
    for pattern in patterns:
        if pattern in lower_name:
            return True
    return False


def filter_mods(mod_dir: str | Path, auto_exclude: bool = True, manual_excludes: list[str] = None) -> list[Path]:
    """
    Scans the mods directory and returns a list of mods to include based on filtering rules.
    """
    mod_dir = Path(mod_dir)
    manual_excludes = [x.lower() for x in manual_excludes or []]

    if not mod_dir.exists() or not mod_dir.is_dir():
        logger.error(f"Mod directory does not exist or is not a directory: {mod_dir}")
        return []

    included_mods = []
    excluded_mods = []

    for mod in mod_dir.glob("*.jar"):
        mod_name = mod.name.lower()

        if mod_name in manual_excludes:
            logger.info(f"Excluded (manual): {mod.name}")
            excluded_mods.append(mod)
            continue

        if auto_exclude and is_client_mod(mod_name, DEFAULT_CLIENT_ONLY_PATTERNS):
            logger.info(f"Excluded (auto): {mod.name}")
            excluded_mods.append(mod)
            continue

        included_mods.append(mod)
        logger.debug(f"Included: {mod.name}")

    logger.info(f"Included mods: {len(included_mods)}, Excluded mods: {len(excluded_mods)}")
    return included_mods
