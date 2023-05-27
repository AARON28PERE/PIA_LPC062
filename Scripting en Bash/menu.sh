#!/bin/bash
# 
# Ejemplo de Menu en BASH
#
date
    echo "|"
    echo "|---------------------------|"
    echo "|   Menu Principal          |"
    echo "|---------------------------|"
    echo "|1. Net Discover"
    echo "|2. Actual User"
    echo "|3. Hostname"
    echo "|4. Exit"
    echo "|"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $HOME/netdiscover.sh;;
        2) whoami;;
        3) echo "Tu host es:"
                hostname
                echo "saludos";;
        4) echo "Bye!"; exit 0;;
esac
