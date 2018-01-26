#!/usr/bin/python3.5

"""
Ce script permet, à partir d'un csv sans titre col1 = key col2 = val
de créer le ou les fichiers de traduction s'ils n'existent pas et
d'ajouter à la fin du fichier la ligne clé + valeur de traduction.

ATTENTION : faire à la mano : les trad avec des virgules; les clé 
en doublon dans le .csv; les clé présentes sur plusieurs .properties
"""
import os
import csv
from pathlib import Path
def rewriteSortedNoDuplicate(filePath):
    if os.path.isdir(filePath):
        return
    with open(filePath) as f:
        rows = f.readlines()
        rows = [x.strip() for x in rows]
        rows.sort()
        rows = list(set(rows))
        for row in rows:
            keyValueTab = row.split('=')
            key = keyValueTab[0].strip()
            index = rows.index(row)
            for row2 in rows:
                index2 = rows.index(row2)
                if index2 == index:
                    continue
                key2 = row2.split('=')
                key2 = key2[0].strip()
                    
                if key2 == key :
                    print('\n'+filePath)
                    print('EFFACEMENT DE CLE EN DOUBLE >>> ' + row2)
                    rows.remove(row2)

        f = open(filePath, 'w')
        for row in rows:
                f.write(row + "\n")
### variables à modifier avant de lancer le script
directoryPath = '/home/lyd/csvTradToProperties' #user_input = input('What is the name of your directory')
folder = directoryPath + '/' 
csvFile = folder + 'csv.csv'
csvLang = 'nl_NL'
###
directory = os.listdir(directoryPath)
with open(csvFile, newline='') as f:
    reader = csv.reader(f)
    foundedFrPropertiesFileNb = 0
    nbAddedLine = 0
    for row in reader: # pour chaque ligne du csv
        rowTab = row[0].split(';')
        key = rowTab[0]
        searchstring = key #searchstring = input('What word are you trying to find?')
        # création pathTradFile en le cherchant
        foundedFrPropertiesFile = False
        for fname in directory:
            nbFileFound = 0
            if os.path.isfile(directoryPath + os.sep + fname):
                f = open(directoryPath + os.sep + fname, 'r')
                if searchstring in f.read():
                    if "_fr_FR.properties" in fname: 
                        foundedFrPropertiesFile = True
                        foundedFrPropertiesFileNb += 1

                        nlFile = fname.replace('fr_FR.properties', csvLang + '.properties') #print('On va ajouter la ligne dans ' + nlFile)

                        nbFileFound += 1
                f.close()
        if nbFileFound > 1:
            print('Cle trouvé en double : ' + key)
        if not foundedFrPropertiesFile:
            print(key + 'NOT FOUND IN A fr_FR PROPERTIES FILE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        pathTradFile = folder + nlFile
        tradNl = rowTab[1]
        line = key + ' = ' + tradNl
        my_file = Path(pathTradFile)
        if not my_file.is_file():
            open(pathTradFile, 'a').close()
        file = open(pathTradFile, 'a')
        toBeWriten = line # or line
        file.write('\n' + toBeWriten + '\n')
        file.close()
        nbAddedLine += 1


        rewriteSortedNoDuplicate(directoryPath + os.sep + nlFile)

        #on enlève les duplicates
            # lines = open(pathTradFile, 'r').readlines()
            # lines_set = set(lines)
            # out  = open(pathTradFile, 'w')
            # for line in lines_set:
            #     out.write(line)
        
print('\n\nJob finished :)\n\nNombre de foundedFrPropertiesFile ' + str(foundedFrPropertiesFileNb) + '\net nombre de addedLine ' + str(nbAddedLine))