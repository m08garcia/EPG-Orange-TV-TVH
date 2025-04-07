#!/bin/sh
#
# tv_grab_orange: EPG Orange TV - 3 días de programación
#

PYTHON_SCRIPT="/home/miguel/orange-epg.py"  # Ajusta la ruta si es necesario

dflag=
vflag=
cflag=
qflag=

# Si no se pasan argumentos, se redirige directamente al script Python
if [ $# -lt 1 ]; then
    exec python3 "$PYTHON_SCRIPT"
fi

# Traducir opciones largas a cortas
for arg in "$@"; do
    delim=""
    case "$arg" in
       --description) args="${args}-d " ;;
       --version) args="${args}-v " ;;
       --capabilities) args="${args}-c " ;;
       --quiet) args="${args}-q " ;;
       *) [[ "${arg:0:1}" == "-" ]] || delim="\""
          args="${args}${delim}${arg}${delim} " ;;
    esac
done

# Restablecer los parámetros posicionales a las opciones cortas
eval set -- $args

while getopts "dvcq" option; do
    case $option in
        d) dflag=1 ;;
        v) vflag=1 ;;
        c) cflag=1 ;;
        q) qflag=1 ;;
        \?) printf "Opción desconocida: -%s\n" "$OPTARG"
            printf "Uso: %s [--description] [--version] [--capabilities]\n" "$(basename $0)"
            exit 2 ;;
    esac >&2
done

if [ "$dflag" ]; then
   printf "EPG Orange TV\n"
fi
if [ "$vflag" ]; then
   printf "6.0\n"
fi
if [ "$cflag" ]; then
   printf "baseline\n"
fi
if [ "$qflag" ]; then
   printf ""
fi

exit 0
