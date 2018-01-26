#!/usr/bin/python3.5
import os
nbDePasse = 0
strToBeReplaced = "fr-babyliss"
replacementStr = "be-babyliss"

for dname, dirs, files in os.walk("/home/lyd/trad/be"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        #s = s.replace(strToBeReplaced, replacementStr)
        s = s.replace('fr-FR', 'fr-BE')
        s = s.replace('fr_FR', 'fr_BE')
        s = s.replace('babyliss-fr', 'babyliss-be')
        s = s.replace('fr-babyliss', 'be-babyliss')
        nbDePasse += 1; 
        with open(fpath, "w") as f:
            f.write(s)
print('Nb de passe : ' + str(nbDePasse))