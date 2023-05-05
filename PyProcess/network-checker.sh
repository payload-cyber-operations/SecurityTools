#!/bin/bash


echo "[*] Networking tool"
echo "[*] the current day $(date +%d)"
echo "[*] $(date +%Y-%m-%d-%H-%M-%S) the current date $(date)" >> logger.log

function checkStatus(){
    if [ -z $2 ]; then
        echo "the second argument it's not availbale"
    else
        echo "This is the second parameter $2"
    fi
    netstat -nat | grep -i "$1"
}

checkStatus "listen"


