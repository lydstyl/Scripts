#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Extraction ou exportation de fichiers .properties via un csv
"""
import os

userChoice = int(input('Votre choix ?'))

def one():
    print("Choice 1 : ressourcesExtractor.py \n")

def two():
    print("Choice 2 \n")
    os.system("rie_c.py 1")

def three():
    print("Is a prime number\n")

# map the inputs to the function blocks
options = {0 : zero,
           1 : one,
           2 : two,
           3 : three
}

options[userChoice]()