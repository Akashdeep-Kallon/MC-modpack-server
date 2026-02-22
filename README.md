# Modpack Repository — AutoModUpdater

Este repositorio contiene los archivos oficiales del modpack que utiliza **AutoModUpdater** para mantener los mods sincronizados automáticamente en todos los clientes.

El repositorio actúa como fuente central desde donde el mod descarga, verifica y actualiza los mods cada vez que se inicia Minecraft.

---

## Qué hace este repositorio

Este repositorio almacena:

* Todos los mods del modpack (`/mods`)
* El archivo `manifest.json`, que describe qué mods deben instalarse y sus hashes de verificación

Cuando un jugador inicia Minecraft con AutoModUpdater instalado:

1. El mod descarga `manifest.json`
2. Comprueba los mods locales del jugador
3. Descarga o actualiza los que falten o estén desactualizados
4. Si hubo cambios, Minecraft se cierra automáticamente para aplicar los mods
5. Si todo está actualizado, el juego continúa normalmente

Esto garantiza que todos los jugadores tengan exactamente los mismos mods y versiones.

---

## Estructura del repositorio

```
/
├── manifest.json
└── mods/
    ├── mod1.jar
    ├── mod2.jar
    └── ...
```

### manifest.json

Define qué mods deben instalarse, desde dónde descargarlos y su hash de seguridad.

Ejemplo:

```
{
  "version": "1.0",
  "mods": [
    {
      "name": "examplemod.jar",
      "url": "RUTA_DE_DESCARGA",
      "sha256": "HASH_DEL_ARCHIVO"
    }
  ]
}
```

---

## Cómo usar este repositorio (administradores del modpack)

Si administras el servidor o el modpack, sigue estos pasos para añadir o actualizar mods.

### 1. Añadir o actualizar un mod

Coloca el archivo `.jar` dentro de la carpeta:

```
/mods/
```

### 2. Subir los cambios

Haz commit y push al repositorio.

### 3. Generación del manifest

El archivo `manifest.json` se genera automáticamente mediante GitHub Actions.

Este proceso:

* detecta los mods dentro de `/mods`
* calcula el hash SHA256 de cada archivo
* actualiza el manifest

No es necesario editar el manifest manualmente.

---

## Cómo lo usan los jugadores

Los jugadores solo necesitan:

1. Instalar Minecraft Forge 1.12.2
2. Colocar el mod AutoModUpdater en su carpeta `/mods`
3. Iniciar el juego normalmente

El sistema se encarga automáticamente de:

* descargar los mods necesarios
* actualizarlos cuando cambien
* mantener el modpack sincronizado

No se requiere instalación manual del modpack.

---

## Seguridad e integridad

Cada mod incluye un hash SHA256 en el manifest.

Esto asegura que:

* los archivos no estén corruptos
* los mods no hayan sido modificados
* todos los clientes tengan versiones idénticas

---

## Uso previsto

Este repositorio está diseñado para distribución automática del modpack mediante AutoModUpdater.

https://github.com/Akashdeep-Kallon/MC-AutoModpackUpdater

Su propósito es mantener sincronizados los mods entre el servidor y todos los clientes de forma automática.

---

## Requisitos

* Minecraft Forge 1.12.2
* Mod AutoModUpdater instalado en el cliente

---
