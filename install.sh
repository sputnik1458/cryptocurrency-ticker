#!/usr/bin/env bash

USER_HOME=$(eval echo ~${SUDO_USER})

cp -r ${USER_HOME}/Cryptocurrency-Ticker/.conkyrc ${USER_HOME}

chmod +x ${USER_HOME}/Cryptocurrency-Ticker/cryptocurrency-ticker.py

crontab -l > mycron
echo "*/5 * * * * ${USER_HOME}/Cryptocurrency-Ticker/cryptocurrency-ticker.py" >> mycron
crontab mycron
rm mycron       

conky &

echo done
