# {modpack_name} - Dedicated Server Pack

Welcome! This package contains everything needed to run a standalone Minecraft server for **{modpack_name}**.

---

## 🧱 Server Info

- **Minecraft Version**: {mc_version}
- **Modloader**: {modloader} {modloader_version}
- **Recommended RAM**: {jvm_args}

---

## 📦 What's Included

- Cleaned mods folder (client-only mods removed)
- `configs`, `kubejs`, `defaultconfigs`, and other resources
- Pre-installed Forge server JAR
- This README

---

## 🚀 Launching Your Server

```bash
java -Xms{jvm_args} -Xmx{jvm_args} -jar forge-{modloader_version}.jar nogui

Be sure to accept the EULA in eula.txt first!

## 🛠 Customization Tips
- You can change memory settings in your launch script
- To add plugins/mods, drop them into the mods folder
- Adjust settings in server.properties, kubejs, or configs as needed

# Happy hosting!

