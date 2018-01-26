#!/usr/bin/python3.5
# coding: utf-8 

"""
Ce script permet, à partir d'un csv de modifier les .properties
FILE	Key 	trad(nl_NL ou autre lang)

ATTENTION : faire à la mano : les trad avec des virgules; les clé 
en doublon dans le .csv; les clé présentes sur plusieurs .properties
"""
import csv
import os

csvPath = '/home/lyd/csvTradToProperties/csv.csv' #
propPath = '/home/lyd/babyliss/conair-uk/cartridges/app_babyliss_fr/cartridge/templates/resources/' #

def getPropFileList(csvPath):
    csvPropFileList = [] # [[file1, {key:val, key2:val2}], [file1, {key:val, key2:val2}], ...]
    with open(csvPath, newline='') as f:
        reader = csv.reader(f, delimiter='§', quotechar='"')
        goNext = False
        for row in reader:
            if goNext == False:
                goNext = True
                continue
            propFile = row[0].strip() # eg locale_nl_NL.properties
            key = row[1].strip()
            val = row[2].strip()

            propFileFound = False
            for fileTab in csvPropFileList:
                if fileTab[0] == propFile :
                    propFileFound = True
                    fileTab[1][key] = val
            if propFileFound == False:
                fileTab = []
                fileTab.append(propFile)
                fileTab.append({key: val})
                csvPropFileList.append(fileTab)
    return csvPropFileList
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
                value = sep.join(key_value[1:]).strip().strip('"') 
                props[key] = value 
    return props
def keyExist(key, filePath):
    """
    Retourne True si la clé existe sinon False
    eg : 
        key = 'account.addressbook.editaddress.editaddress'
        filePath = '/home/lyd/resources/account_fr_FR.properties'
        print(keyExist(key, filePath))
    """
    lesProps = loadProperties(filePath)
    try:
        lesProps[key]
        return True
    except: 
        pass
    return False
def rewriteProperties(propertiesFilePath, propertiesKeyVal):
    print('\n\n')
    print(propertiesKeyVal)
def addOrCreate(propertiesFilePath, keyToAdd, valToAdd):
    if not os.path.exists(propertiesFilePath):
        propertiesFile = open(propertiesFilePath, 'a')
        propertiesFile.close()
    props = loadProperties(propertiesFilePath)
    props[keyToAdd] = valToAdd
    lines = []
    for key, val in props.items():

        string = key + ' = ' + val + '\n'
        # string = string.encode('iso-8859-1') # does this fix encoding issues with ressource bundle ? Livraison \u00C3\u00A0
        # généré par python > global.createnowbutton = Cr\u00E9er un compte > FAIL (prblème d'accent)
        # généré par ResourceBundle > global.createnowbutton = cr\u00C3\u00A9er un compte > FAIL
        # généré par python puis par bundle > Cree\u00C3\u00ABr account > SUCCESS (fonctionne)
        lines.append(string)

    lines.append('# Generated by a Python script in Altima\n')
    lines.sort()
    propertiesFile = open(propertiesFilePath, 'w')
    propertiesFile.writelines(lines)
    propertiesFile.close()

propFileList = getPropFileList(csvPath)
for fileTab in propFileList:
    fileName = fileTab[0]
    keyValDict = fileTab[1]
    for key, val in keyValDict.items():
        addOrCreate(propPath + fileName, key, val)