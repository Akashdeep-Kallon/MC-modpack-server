import os, hashlib, json

# Carpeta con los mods
mods_folder = "mods"
# Base URL para raw GitHub
base_url = "https://raw.githubusercontent.com/USUARIO/REPO/main/mods/"

manifest = {
    "version": "1.0",
    "mods": []
}

# Generar SHA256 y URLs
for mod_file in os.listdir(mods_folder):
    if mod_file.endswith(".jar"):
        sha256_hash = hashlib.sha256()
        with open(os.path.join(mods_folder, mod_file), "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        manifest["mods"].append({
            "name": mod_file,
            "url": base_url + mod_file,
            "sha256": sha256_hash.hexdigest()
        })

# Guardar manifest.json
with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("Manifest generado automáticamente con éxito.")