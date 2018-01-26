#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""

"""
import csv, os
#### VARIABLES A RENSEIGNER AVANT DE LANCER LE SCRIPT
langCod = 'all_lang'

ressourceFolder = '/home/lyd/trad/' + langCod
csvFolder = '/home/lyd/trad'
csvName = langCod + '_properties'
theDelimiter = '§'
####
keyValTab = []
def loadProperties(filePath):
    """
    Read the file passed as parameter as a properties file.
    """
    sep='='
    comment_char='#'
    props = {}
    with open(filePath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"').strip()
                props[key] = value 
    return props

rows = []
with open(csvFolder + '/' + csvName + '.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=theDelimiter,
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    titleRow = ['FILE',	'FR_KEY', 'FR_VAL',	'NL_VAL']
    rows.append(titleRow)
    for element in os.listdir(ressourceFolder):
        if '_fr_BE' in element: # _fr_BE puis _nl_BE
            properties = loadProperties(ressourceFolder + '/' + element)
            for key in properties:
                keyVal = key + properties[key]
                keyValTab.append(keyVal)
                row = [element, key, properties[key], '']
                rows.append(row)
    try:
        l = -1
        for row in rows:
            l += 1
            if l == 0:
                continue
            nlFile = row[0].replace("_fr_BE", "_nl_BE")
            for element in os.listdir(ressourceFolder):
                if '_nl_BE' in element:
                    properties = loadProperties(ressourceFolder + '/' + element)
                    for key in properties:
                        if key.strip() == row[1].strip():
                            val = properties[key]
                            row[3] = val
    except:
        pass

    for row in rows:
        spamwriter.writerow(row)