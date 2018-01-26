#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Script de test
"""
import subprocess
# subprocess.call(["ls", "-l"])
# subprocess.call(['startGulp.sh']) & subprocess.call(['startEclipse.sh']) 
# subprocess.call(['startEclipse.sh'])



# NL
# 	regex
# 	recette
# BE 
# 	url

# footer global tous les sites


# python start + choix


import multiprocessing

def worker(file):
    #your subprocess code
    subprocess.call([file])


if __name__ == '__main__':
    files = ["ls","gnome-terminal","gnome-terminal"]
    for i in files:
        p = multiprocessing.Process(target=worker(i))
        p.start()