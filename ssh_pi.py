#!/usr/bin/env python3.5
# -*- coding: UTF8 -*-

"""
Permet de se connecter au pi en ssh en wifi ou en ethernet

"""



import os

choix_connexion = input("En wifi --> w \n\nou alors \n\nEn RJ45 --> e . \
Votre choix ? ")
if choix_connexion == "w":
	modif_ip = "17"
else:
	modif_ip = "42"

commande = "ssh pi@192.168.0." + modif_ip

os.system(commande)
