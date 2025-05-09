# CLI/main.py

import argparse
from pathlib import Path

from utils.logger import setup_logger
from core.config_loader import load_config, init_config
from core.mod_filter import filter_mods
from core.file_manager import prepare_output_directory, copy_server_files
from core.forge_installer import install_forge
from core.packager import clean_temp_files, generate_readme, zip_server_pack

CONFIG_PATH = Path("config.yaml")
DEFAULT_CONFIG_PATH = Path("templates/default_config.yaml")

logger = setup_logger("main")


def run_pipeline():
    config = load_config(CONFIG_PATH)

    modpack_path = Path(config["modpack"]["path"])
    output_path = Path(config["output"]["directory"])
    includes = config["modpack"].get("include_dirs", [])
    manual_excludes = config["modpack"].get("manual_excludes", [])

    # Prepare output directory
    prepare_output_directory(output_path)

    # Copy necessary files
    copy_server_files(modpack_path, output_path, includes, manual_excludes)

    # Filter mods
    mods_dir = output_path / "mods"
    filter_mods(mods_dir, config["modpack"]["auto_exclude_client"])

    # Install Forge
    if config["server"]["jar"]["auto_download"]:
        install_forge(
            mc_version=config["server"]["jar"]["version"],
            loader_version=config["server"]["jar"]["modloader_version"],
            output_dir=output_path
        )

    # Generate README
    context = {
        "modpack_name": modpack_path.name,
        "mc_version": config["server"]["jar"]["version"],
        "modloader": config["server"]["jar"]["modloader"],
        "modloader_version": config["server"]["jar"]["modloader_version"],
        "jvm_args": f"{config['jvm']['memory']['initial']} - {config['jvm']['memory']['max']}"
    }

    if config["output"]["include_readme"]:
        generate_readme(config["output"]["readme_template"], output_path, context)

    # Cleanup & Package
    clean_temp_files(output_path)
    zip_server_pack(
        serverpack_dir=output_path,
        output_dir=output_path.parent,
        name_template=config["output"]["zip_name"],
        context=context
    )


def main():
    parser = argparse.ArgumentParser(description="Minecraft ServerPack Generator CLI")
    parser.add_argument("--init", action="store_true", help="Generate default config.yaml from template.")
    parser.add_argument("--build", action="store_true", help="Run the server pack generation pipeline.")
    args = parser.parse_args()

    if args.init:
        init_config(CONFIG_PATH, DEFAULT_CONFIG_PATH)
    elif args.build:
        run_pipeline()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
