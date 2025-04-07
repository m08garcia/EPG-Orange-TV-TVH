### Guía de instalación de la EPG de Orange TV España para Tvheadend

![alt text](https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/master/imagenes/Screenshot_20250407_125443.png)

(Los picons o iconos de canal no están incluidos en este script EPG)

El Script por efecto descarga 5 días de EPG (El actual y los 4 siguientes), si quiere modificar este número en el script de python modifique esta línea:
```shellscript
def get_epg(self, days={Número de días}):
```

## Requisitos previos

- Python 3
- Python Requests (Auto-intalado por el script automático)
- Permisos de administrador (sudo)

## Instalación automática

Para instalar automáticamente, ejecuta el siguiente comando:

```shellscript
curl -sSL https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/main/instalar.sh | sudo bash
```

Luego en el panel de TVHeadend vaya a Configuración 🡪 Canal / EPG 🡪 Módulos para Obtención de Guia y habilite el que se llame: XMLTV: EPG Orange TV.

![alt text](https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/master/imagenes/Screenshot_20250407_124856.png)

## Instalación de Python (Sí no está ya instalado)

### En Debian/Ubuntu

```shellscript
sudo apt update && sudo apt install python3 python3-pip
```

### En Fedora

```shellscript
sudo dnf install python3 python3-pip
```

### Para otras distribuciones consultar aquí:
https://gist.github.com/MichaelCurrin/57d70f6aaba1b2b9f8a834ca5dd19a59


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

6. **Reiniciar TVHeadend**:
```shellscript
sudo systemctl restart tvheadend
```
7. **Habilitar el módulo de EPG en TVH**:
En el panel de TVHeadend vaya a Configuración 🡪 Canal / EPG 🡪 Módulos para Obtención de Guia y habilite el que se llame: XMLTV: EPG Orange TV.
![alt text](https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/master/imagenes/Screenshot_20250407_124856.png)
   
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
