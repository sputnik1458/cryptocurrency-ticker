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
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/btc/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    return price

def Ethereum():
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    return price

def Monero():
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/xmr/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    return price

def file_write(bitcoin, ethereum, monero):
    file = open("/home/jacob/Code/Python/prices.txt", 'w')
    file.write("\nBitcoin:$%.2f\n" % bitcoin)
    file.write("Ethereum: $%.2f\n" % ethereum)
    file.write("Monero: $%.2f" % monero)
    file.close

parse()
