#!/usr/bin/python3.5
"""
Mon premier script orienté objet qui permet de renommer les fichiers 
d'un dossier quelque soit son extension si elle existe ou non 
et sans renommer les dossiers
"""
import os, re
class Fichier:
    def __init__(self):
        self.path = str(input("Chemin du dossier ?"))
        if self.path[len(self.path) - 1] != "/":
            self.path += "/"
    def renomer(self):
        self.prefix = str(input('Prefix ?'))
        self.sufix = str(input('Sufix ?'))
        self.fichiers = os.listdir(self.path)
        i = 0
        for fichier in self.fichiers:
            if os.path.isdir(self.path + fichier):
                continue
            i += 1
            num = str(i)
            extension = re.findall('.[a-zA-Z]{2,4}$', fichier)
            if not extension:
                extension = ''
            else:
                extension = extension[0]
            os.rename(self.path + fichier, self.path + \
                self.prefix + num + self.sufix + extension)
    def renomerSansExtension(self):
        demanderPreEtSufix(self)
        i = 0
        for fichier in self.fichiers:
            if os.path.isdir(self.path + fichier):
                continue
            i += 1
            num = str(i)
            os.rename(self.path + fichier, self.path + \
                self.prefix + num + self.sufix)
    def demanderPreEtSufix(self):
        self.prefix = str(input('Prefix ?'))
        self.sufix = str(input('Sufix ?'))
        self.fichiers = os.listdir(self.path)
