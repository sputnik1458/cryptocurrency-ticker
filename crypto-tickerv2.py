#! /usr/bin/env python

import requests
from bs4 import BeautifulSoup
import json

def parse():
    bitcoin = Bitcoin()
    ethereum = Ethereum()
    monero = Monero()
    file_write(bitcoin, ethereum, monero)

def Bitcoin():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    info.append(price)
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/volume"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    info.append(volume)
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/change"
    e = requests.get(change_url)
    change = e.json()
    info.append(change)
    return info

def Ethereum():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/volume"
    info.append(price)
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    info.append(volume)
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/change"
    e = requests.get(change_url)
    change = e.json()
    info.append(change)
    return info

def Monero():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/volume"
    info.append(price)
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    info.append(volume)
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/change"
    e = requests.get(change_url)
    change = e.json()
    info.append(change)
    return info

def file_write(bitcoin, ethereum, monero):
    bitprice = bitcoin[0]
    bitvolume = bitcoin[1]
    bitchange = bitcoin[2]
    ethprice = ethereum[0]
    ethvolume = ethereum[1]
    ethchange = ethereum[2]
    xmrprice = monero[0]
    xmrvolume = monero[1]
    xmrchange = monero[2]
    file = open("prices.txt", 'w')
    file.write("\nBitcoin: \n Price: $%.2f \n 24h Volume: $%s\n 24h Change: %s%% \n" % (bitprice, format(bitvolume, ','), bitchange))
    file.write("Ethereum: \n Price: $%.2f\n 24h Volume: $%s\n 24h Change: %s%% \n" % (ethprice, format(ethvolume, ','), ethchange))
    file.write("Monero: \n Price: $%.2f\n 24h Volume: $%s\n 24h Change: %s%%" % (xmrprice, format(xmrvolume, ','), xmrchange))
    file.close

parse()
