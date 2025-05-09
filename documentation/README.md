# Minecraft ServerPack Generator

A Python-based tool that converts client-side Minecraft modpacks into a fully functional, server-ready package. It supports Forge and other modloaders, with the ability to filter out client-side mods, configure server settings, and package the server for easy deployment.

---

## ⚙️ Features

- **Automatic Forge Installation**: Installs Forge server JAR automatically based on config.
- **Mod Filtering**: Excludes client-only mods and includes only the necessary ones for the server.
- **Configurable Server Settings**: Easily set JVM memory args, Forge version, and other server settings in `config.yaml`.
- **Cross-Platform Support**: Generates `run.bat` for Windows and `run.sh` for Linux/macOS.
- **Clean Packaging**: Zips the final server pack with mod files, configurations, and documentation.
- **Custom README Template**: Generates a customizable README for your server pack.

---

## 🛠 Requirements

- Python 3.10+
- `pyyaml`
- `requests`
- `tqdm`

To install dependencies, run:

```bash
pip install -r requirements.txt


## 🚀 Getting Started
1. Clone the Repository
    git clone https://github.com/yourusername/minecraft-serverpack-generator.git
    cd minecraft-serverpack-generator

2. Initialize the Config
Run the init command to generate a config.yaml from the default template:
    python CLI/main.py --init

3. Build the Server Pack
Once the config.yaml is ready, run the build command to generate your server pack:
    python CLI/main.py --build
The generated server pack will be in the serverpack/ directory.

## 🛠 Configuration
The configuration is stored in config.yaml. You can modify the following:
- modpack.path: Path to your client-side modpack folder.
- server.jar.version: Minecraft version (e.g., 1.20.1).
- server.modloader: Type of modloader (forge currently supported).
- server.modloader_version: The version of Forge to install (e.g., 47.4.0).
- output.directory: Path to save the generated server pack.

Example of a typical config:
    modpack:
    path: "./modpack"
    auto_exclude_client: true
    manual_excludes: []
    include_dirs:
        - "configs"
        - "kubejs"
        - "defaultconfigs"
        - "blueprints"

    server:
    jar:
        auto_download: true
        version: "1.20.1"
        modloader: "forge"
        modloader_version: "47.4.0"

    jvm:
    memory:
        initial: "2G"
        max: "4G"
    extra_args: ""

    output:
    directory: "./serverpack"
    create_zip: true
    zip_name: "{modpack_name}_serverpack"
    include_readme: true

## 📦 Outputs
- Server Pack: The final output is a .zip file containing all necessary files to run your server.
- README: A customized README file is generated based on readme_template.md.

## 🧩 Extending the Project
- New Modloaders: You can extend the project to support additional modloaders (e.g., Fabric) by modifying the forge_installer.py.
- Docker Support: Future support for generating a Dockerized version of the server.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-xyz)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature-xyz)
5. Create a new Pull Request

## 📢 Acknowledgements
- Forge
- Python
- PyYAML
- Requests



---

### Key Sections in the README:

1. **Features**: A brief summary of the tool’s key capabilities.
2. **Requirements**: List of Python and package dependencies needed to run the tool.
3. **Getting Started**: Step-by-step guide for cloning the repo, initializing the config, and building the server pack.
4. **Configuration**: Explains the `config.yaml` and key parameters you can modify.
5. **Outputs**: Description of the final output (the `.zip` file and README).
6. **Extending the Project**: Guidance for extending functionality, such as adding support for other modloaders or Docker.
7. **License**: MIT License (or whichever license you're using).
8. **Contributing**: How others can contribute to the project.

---

This README serves as both a guide for users and a good starting point for contributors. 

