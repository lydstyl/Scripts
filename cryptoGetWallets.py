#!/usr/bin/python3.5
# vim : set fileencoding=utf-8 :
# script créé par Gabriel Brun

"""
Ce script permet d'obtenir l'ensemble des balances de mes wallets qui ont une API. Il fonctionne avec des scripts NodeJS.
"""

import subprocess
# p = subprocess.Popen(['commande', 'option1', 'arg1', 'option2', 'arg2'], stdout=subprocess.PIPE, shell=True)


ttrex = subprocess.Popen(['node ~/Dropbox/Informatique/Node.js/crypto/getWalletsBalances/ttrex.js'], stdout=subprocess.PIPE, shell=True).stdout.read()
ttrex = ttrex.replace('lydBittrex', 'Bittrex')

poloniex = subprocess.Popen(['node ~/Dropbox/Informatique/Node.js/crypto/poloniex/poloniex.js'], stdout=subprocess.PIPE, shell=True).stdout.read()

stamp = subprocess.Popen(['node ~/Dropbox/Informatique/Node.js/crypto/getWalletsBalances/stamp.js'], stdout=subprocess.PIPE, shell=True).stdout.read()
stamp = 'Bitsamp --> ' + stamp

binance = subprocess.Popen(['node ~/Dropbox/Informatique/Node.js/crypto/getWalletsBalances/lydBinance.js'], stdout=subprocess.PIPE, shell=True).stdout.read()
binance = binance.replace('lydBinance', 'Binance')


string = stamp + binance + ttrex + poloniex 
# Bitsamp --> BTC: 0.51830545; XRP: 0.00000003
# Binance --> BTC: 0.00016395; ETH: 0.00008558; NEO: 6; BNB: 9.8957847; BCC: 0.05994; IOTA: 264.735; DASH: 0.1998; XMR: 2.5477; ADA: 3725.271; WAVES: 10;
# Bittrex --> AEON: 30; BTC: 6.4e-7; ETH: 0; GNT: 275.37904429; NEO: 15.837387; QTUM: 29.96172062; XEM: 250; XLM: 200; XRP: 4.42564
# Ploloniex --> BCH: 1.00000000; BTC: 0.02998181; ETH: 0.03862996; XEM: 608.47411120; XMR: 2.77499998
print(string)