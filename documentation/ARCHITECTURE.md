# Project Architecture - Minecraft ServerPack Generator

## Overview

This tool generates a Minecraft server-ready distribution package from a client modpack folder. It supports Forge (and future support for Fabric), client-side mod filtering, packaging, and documentation generation.

---

## 📁 Project Structure

serverpack_generator/
│
├── CLI/ # CLI entrypoint (main.py)
│
├── core/ # Core logic and utility modules
│ ├── config_loader.py # Loads and validates YAML config
│ ├── file_manager.py # Handles copying files to output
│ ├── mod_filter.py # Filters out client-side mods
│ ├── forge_installer.py # Auto-installs Forge server JARs
│ ├── packager.py # Cleans, generates README, and zips
│ └── logger.py # Centralized logging utility
│
├── documentation/
│ ├── ARCHITECTURE.md # You are here
│ ├── README.md # GitHub/Project-level info
│ └── readme_template.md # Used inside server pack outputs
│
├── templates/
│ └── default_config.yaml # Default YAML config used at init
│
├── temp/ # Runtime log and temp output directory
│
└── config.yaml # User-generated config (via --init)

---

## 🔁 Workflow Pipeline

1. `main.py --init` → Copies `default_config.yaml` to `config.yaml`
2. `main.py --build` → Executes:
    - Load `config.yaml`
    - Prepare output dir
    - Copy and clean files
    - Filter client-side mods
    - Install Forge (if enabled)
    - Generate README from `readme_template.md`
    - Zip final package

---

## 📚 Dependencies

- Python 3.10+
- `pyyaml`, `requests`, `tqdm`
- Logging to `temp/logs/serverpack.log`

---

## 🧩 Modularity & Extensibility

- Support for additional modloaders (e.g. Fabric) can be added to `forge_installer.py`
- GUI frontend can reuse core logic via import
- Config fields are cleanly namespaced: `modpack`, `server`, `jvm`, `output`

---

## 🗂 Planned Modules

- `fabric_installer.py` (future)
- `mod_analyzer.py` (for unsafe mod validation)
