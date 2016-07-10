#!/usr/bin/env bash

USER_HOME=$(eval echo ~${SUDO_USER})

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cp -r ${DIR}/.conkyrc ${USER_HOME}

chmod +x ${DIR}/crypto-tickerv2.py

touch $USER_HOME/prices.txt

crontab -l > mycron
echo "*/5 * * * * ${DIR}/crypto-tickerv2.py" >> mycron
crontab mycron
rm mycron

${DIR}/crypto-tickerv2.py 

pkill conky
conky </dev/null &>/dev/null &

echo done
