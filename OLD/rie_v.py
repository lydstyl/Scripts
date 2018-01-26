#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
riev
"""
def alreadyInPropertiesFile(key, val, propertiesFile):
    print(key + '=' + val + ' déjà dans ' + propertiesFile + ' donc on passe.')
def errorWhenWriting(propertiesFile, keyVal):
    print('Error when writing in ' + propertiesFile + ' the key and val ' + keyVal)
def ouch(l, row, rowTab):
    print('\n\AOUCH ligne ' + str(l) + ' !')
    print(row)
    print(rowTab)
def param(folder, csvFile):
    print('PARAMETRES DU SCRIPT :\nfolder -> ' + folder, '\ncsvFile -> ' + csvFile + '\n')