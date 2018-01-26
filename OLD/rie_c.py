#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
RIE_C = Ressources import export controller
"""
from rie_helper import *
rie_v.param(folder, csvFile)
l = 0  # row number
for rowTab in csvReader(aNewLine, aDelimiter, aQuotechar): # for each row in the csv
    l += 1
    propertiesFile = rowTab[0]
    if isTitleRow(propertiesFile):
        continue
    try:
        keyVal = rowTab[1]
        key = rowTab[2]
        val = rowTab[3]
        # doublon = rowTab[4]
    except Exception:
        rie_v.ouch(l, row, rowTab)
        continue
        pass
    propertiesFileContent = createAndReadFile(folder, propertiesFile)
    if key + '=' + val in propertiesFileContent:
        rie_v.alreadyInPropertiesFile(key, val, propertiesFile)
        continue
    else: # adding key and value
        try:
            if not keyExist(key, folder + '/' + propertiesFile):
                writingAtEndOfFile(folder, propertiesFile, key, val)
            else:
                writingInTheRightRow(folder, propertiesFile,key, val)
        except Exception:
            rie_v.errorWhenWriting(propertiesFile, keyVal)
            pass
# todo : ajout d'un fichier log
# ajout fichier de conf