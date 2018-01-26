#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Extract essentials infos from the conten        t xml to a csv
Attention modification du fichier :
        suppression attribut lien sur la première balise <library xmlns="http://www.demandware.com/xml/impex/library/2006-10-31"
        remplacement attribut xml:lang par lang
http://apprendre-python.com/page-xml-python-xpath
http://blog.norore.fr/index.php?article14/parser-un-fichier-xml-avec-espaces-nommes-a-coup-de-python

 xmlns="http://www.demandware.com/xml/impex/metadata/2006-10-31"
"""
import csv
from lxml import etree

fileName = "sysObjectTypeBE3"

fichier = fileName + ".xml"
csvFile = fileName + '.csv'
arbre = etree.parse(fichier)
csvfile = open(csvFile, 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter='§', quotechar='"', quoting=csv.QUOTE_MINIMAL)

spamwriter.writerow(['ATTRIBUTE ID', 'NAME','FR', 'NL'])
for noeud in arbre.xpath('//metadata'):
        for typeExtension in noeud.iter('type-extension'):
                for customAttributeDefinitions in typeExtension.iter('custom-attribute-definitions'):
                        for attributeDefinition in customAttributeDefinitions.iter('attribute-definition'):
                                attributeId = attributeDefinition.get('attribute-id')
                                for displayName in attributeDefinition.iter('display-name'):
                                        lang = displayName.get('lang')
                                        if lang == "fr-BE":
                                                frDisplayNameStr = displayName.text
                                        if lang == "nl-BE":
                                                nlDisplayNameStr = displayName.text
                                                spamwriter.writerow([attributeId, 'display-name', frDisplayNameStr, nlDisplayNameStr])
                                for valueDefinitions in attributeDefinition.iter('value-definitions'):
                                        for valueDefinition in valueDefinitions.iter('value-definition'):
                                                for display in valueDefinition.iter('display'):
                                                        lang = display.get('lang')
                                                        if lang == "fr-BE":
                                                                frDisplayStr = display.text
                                                        if lang == "nl-BE":
                                                                nlDisplayStr = display.text
                                                                spamwriter.writerow([attributeId, 'display', frDisplayStr, nlDisplayStr])