#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
Helper
"""
import csv
import os
import rie_v
from rie_conf import *
def createAndReadFile(folder, propertiesFile):
    file = open(folder + '/' + propertiesFile, 'a') # si le fichier n'existe pas on le créé
    file.close()
    file = open(folder + '/' + propertiesFile, 'r') # on lit le fichier
    content = file.readlines()
    file.close()
    content = [x.strip() for x in content] # enlève les saut de ligne dans le tableau
    return content
def csvReader(aNewLine, aDelimiter, aQuotechar):
    csvfile = open(folder + '/' + csvFile, newline=aNewLine) # open the csv file
    reader = csv.reader(csvfile, delimiter=aDelimiter, quotechar=aQuotechar) # FILE;KEY=VAL;KEY;VAL;DOUBLON
    return reader
def fileExist(pathToFile):
    """
        Retourne true si le fichier exist
    """
    my_file = Path(pathToFile)
    if my_file.py():
        return True
    return False
def isTitleRow(propertiesFile):
    if propertiesFile == 'FILE':
        return True 
    return False
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
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    print('remplacement de la ligne '+ str(line_num + 1) +' par ' + text)
    out.close()
def rowNum(propertiesFilePath, key):
    with open(propertiesFilePath) as myFile:
        for num, line in enumerate(myFile, 1):
            if key in line:
                # print('C\'est à dire à la ligne : ' + str(num))
                return num - 1
def writingAtEndOfFile(folder, propertiesFile, key, val):
    file = open(folder + '/' + propertiesFile, 'a')
    print('Ajout à la fin de ' + propertiesFile + ' de ' + key + '=' + val)
    file.write(key + '=' + val)
    file.write('\n')
    file.close()
def writingInTheRightRow(folder, propertiesFile,key, val):
    num = rowNum(folder + '/' + propertiesFile, key)
    print('Dans ' + propertiesFile + ', ')
    replace_line(folder + '/' + propertiesFile, num, key + '=' + val + '\n')