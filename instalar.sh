#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Este script necesita acceso root. Por favor ejecutelo con sudo"
  exit 1
fi

# Get the current user's home directory
CURRENT_USER=$(logname || who | awk '{print $1}' | head -n 1)
USER_HOME=$(eval echo ~$CURRENT_USER)

echo "Installing for user: $CURRENT_USER (home: $USER_HOME)"

# Descargar el script Python desde GitHub
echo "Descargando orange.py..."
curl -s -o "$USER_HOME/orange.py" "https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/main/orange-epg.py"

# Descargar el script bash desde GitHub
echo "Descargando tv_grab_orange_es..."
curl -s -o "/usr/bin/tv_grab_orange_es" "https://raw.githubusercontent.com/m08garcia/EPG-Orange-TV-TVH/main/tv_grab_orange_es"

# Hacer los scripts ejecutables
chmod +x /usr/bin/tv_grab_orange_es
chmod +x "$USER_HOME/orange.py"

# Establecer propiedad correcta para el script Python
chown $CURRENT_USER:$CURRENT_USER "$USER_HOME/orange.py"

# Instalar dependencias
echo "Instalando Python requests package..."
pip install requests --break-system-packages

# Reiniciar TVHeadend
echo "Reiniciando TVHeadend..."
systemctl restart tvheadend

echo "Instalación Completada"
echo "Script de Python instalado en: $USER_HOME/orange.py"
echo "Script bash para TVH en: /usr/bin/tv_grab_orange_es"
echo "Diríjase a TVHeadend > Canal/EPG > Módulos de obtención de Guía y active XMLTV: EPG Orange TV"
