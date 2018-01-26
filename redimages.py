#!/usr/bin/python3.5
# vim : set fileencoding=utf-8 :

#sudo apt-get install python3-pil
#Objectif : redimensionner en masse des images dans un dossier, 
#avant utilisation pour blog ou partage par email par exemple
# TODO : fix si fichier non image présent dans le dossier 
#(genre .directory), fait mais hard codé sur terminaison fichier 
#image en "G" ou "g"

from PIL import Image
import os
from os import listdir, mkdir
from os.path import isfile, join

continuer = "o"
target = 1000
mypath = input("Dans quel dossier sont les images ? ")
if mypath[len(mypath) - 1] != '/':
    mypath += '/'
mypath2 = mypath + "redim"
if not os.path.isdir(mypath2):
    os.mkdir(mypath2) #création du dossier redim
while continuer == "o":
	imageFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
	print("Dimension maximum = " + str(target) + " taper 0 pour garder ou un autre nombre pour changer")
	new_target = 0
	new_target = int(input())
	if new_target != 0:
		target = new_target
	for im in imageFiles :
		im1 = Image.open(join(mypath,im))
		originalWidth, originalHeight = im1.size
		ratio = originalWidth / originalHeight
		if ratio > 1 :
			width = target
			height = int(width / ratio)
		else :
			height = target
			width = int(height * ratio)
		# linear interpolation in a 2x2 environment
		im2 = im1.resize((width, height), Image.ANTIALIAS) 
		im2.save(join(mypath2, "".join([str(width),"x",str(height),"_",im])))
		print (im, "redimensionnée…")
	print ("Travail terminé !", len(imageFiles), "images redimensionnées.")
	continuer = input("Continuer ? o, n ")