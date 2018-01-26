#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Script de test
"""
from lxml import etree

fichier = "fichier.xml"
arbre = etree.parse(fichier)
racine = arbre.getroot()

# for noeud in arbre.xpath('//menu_ptit_dej'):
#     for nom in noeud.xpath('plat/nom'):
#         print(nom.text)
#     for prix in noeud.xpath('plat/prix'):
#         print(prix.text)
#     for calories in noeud.xpath('plat/calories'):
#         print(calories.text)
#     for description in noeud.xpath('plat/description'):
#         print(description.text)

for noeud in arbre.xpath('//menu_ptit_dej'):
    for plat in noeud.iter('plat'):
        for nom in plat.iter('nom'):
                print('test')
                if(nom.get("data-id") != 'None'):
                        print(nom.get("data-id"))
        # print("Nom : {}".format(plat.xpath("nom")[0].text))
