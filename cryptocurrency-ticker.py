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
    return info

def file_write(bitcoin, ethereum, monero):
    bitprice = bitcoin[0]
    bitvolume = bitcoin[1]
    ethprice = ethereum[0]
    ethvolume = ethereum[1]
    xmrprice = monero[0]
    xmrvolume = monero[1]
    file = open("/home/jacob/Code/Python/prices.txt", 'w')
    file.write("\nBitcoin: \n Price: $%.2f \n 24h Volume: $%d\n" % (bitprice, bitvolume))
    file.write("Ethereum: \n Price: $%.2f\n 24h Volume: $%d\n" % (ethprice, ethvolume))
    file.write("Monero: \n Price: $%.2f\n 24h Volume: $%d" % (xmrprice, xmrvolume))
    file.close

parse()
