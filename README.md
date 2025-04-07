### Guía de instalación de Orange TV EPG

## Requisitos previos

- Python 3
- Permisos de administrador (sudo)

## Instalación automática

Para instalar automáticamente, ejecuta el siguiente comando:

```shellscript
curl -sSL https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/main/instalar.sh | sudo bash
```

## Instalación de Python (Sí no está ya instalado)

### En Debian/Ubuntu

```shellscript
sudo apt update && sudo apt install python3 python3-pip
```

### En Fedora

```shellscript
sudo dnf install python3 python3-pip
```

## Instalación manual

Si prefieres instalar manualmente, sigue estos pasos:

### Pasos de instalación

1. **Instalar la dependencia de Python**:

```shellscript
sudo pip install requests --break-system-packages
```

2. **Crear el archivo Python**:
Descarga el script python de obtención `orange.py` en tu directorio home:

```shellscript
sudo wget -P ~ "https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/main/orange.py"
```


4. **Descarga el script bash para TVH**:

```shellscript
sudo wget -P /usr/bin/ -O tv_grab_orange_es "https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/main/tv_grab_orange_es.sh"
```

5. **Hacer ejecutable el script shell**:

```shellscript
sudo chmod +x /usr/bin/tv_grab_orange_es
```


## Verificación

Para verificar que la instalación se realizó correctamente, ejecuta:

```shellscript
tv_grab_orange_es --description
```

Deberías ver el mensaje "EPG Orange TV".

## Desinstalación

Si necesitas desinstalar:

1. Eliminar los scripts:

```shellscript
sudo rm /usr/bin/tv_grab_orange_es
rm ~/orange.py
```


2. Opcionalmente, desinstalar la dependencia de Python (si no la necesitas para otras aplicaciones):

```shellscript
sudo pip uninstall requests
```


## Notas adicionales

- El script Python (`orange.py`) se guarda en el directorio home del usuario actual.
- El script shell (`tv_grab_orange_es.sh`) se instala en `/usr/bin` para que esté disponible en el PATH del sistema.
- Ambos scripts se hacen ejecutables con `chmod +x`.
- La dependencia de Python `requests` se instala con la opción `--break-system-packages` para permitir la instalación.


## Solución de problemas

Si encuentras errores relacionados con Python o las dependencias, asegúrate de que Python 3 y pip estén correctamente instalados en tu sistema.

Para comprobar la versión de Python instalada:

```shellscript
python3 --version
```

Para comprobar la versión de pip instalada:

```shellscript
pip3 --version
```
