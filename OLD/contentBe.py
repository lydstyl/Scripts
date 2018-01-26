#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Extract essentials infos from the content xml to a csv
Attention modification du fichier :
        suppression attribut lien sur la première balise <library xmlns="http://www.demandware.com/xml/impex/library/2006-10-31"
        remplacement attribut xml:lang par lang
http://apprendre-python.com/page-xml-python-xpath
http://blog.norore.fr/index.php?article14/parser-un-fichier-xml-avec-espaces-nommes-a-coup-de-python
"""
import csv
from lxml import etree

fichier = "content-be-babyliss.xml"
csvFile = 'content-be-babyliss.csv'

arbre = etree.parse(fichier)

csvfile = open(csvFile, 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter='§', quotechar='"', quoting=csv.QUOTE_MINIMAL)


rows = []
titleRow = ['REF', 'fr_BE', 'nl_BE', 'SORT', 'TO TRANSLATE AUTO', 'TO TRANSLATE HUMAN']
rows.append(titleRow)

def writeNodeContainer(nodeContainerObject, spamwriter, nodeContainer, contentType, nodeContainerId):
        for nodeContainerObject in nodeContainerObject.iter(nodeContainer):
                ref = nodeContainerId + '>' + contentType
                row = ['', '', '', '', '', '']
                row[0] = ref
                for contentSousTypeObject in nodeContainerObject.iter(contentType):
                        ref = nodeContainerId + '>' + contentType
                        ssType = contentSousTypeObject.get("attribute-id")
                        if ssType is not None:
                                ref += '>' + ssType
                                row[0] = ref
                        if(contentSousTypeObject.get("lang") == 'fr-BE'):
                                row[1] = contentSousTypeObject.text.strip()
                        elif(contentSousTypeObject.get("lang") == 'nl-BE'):
                                row[2] = contentSousTypeObject.text.strip()
                rows.append(row)

for noeud in arbre.xpath('//library'):
        for folder in noeud.iter('folder'):
                nodeContainerId = folder.get('folder-id')
                writeNodeContainer(folder, spamwriter, 'folder', 'display-name', nodeContainerId)
                for refinementDefinitions in folder.iter('refinement-definitions'):
                        writeNodeContainer(refinementDefinitions, spamwriter, 'refinement-definitions', 'display-name', nodeContainerId)
        for content in noeud.iter('content'):
                nodeContainerId = content.get('content-id')
                writeNodeContainer(content, spamwriter, 'content', 'display-name', nodeContainerId)
                writeNodeContainer(content, spamwriter, 'content', 'description', nodeContainerId)
                writeNodeContainer(content, spamwriter, 'custom-attributes', 'custom-attribute', nodeContainerId)
                writeNodeContainer(content, spamwriter, 'page-attributes', 'page-description', nodeContainerId)
                writeNodeContainer(content, spamwriter, 'page-attributes', 'page-keywords', nodeContainerId)
                writeNodeContainer(content, spamwriter, 'page-attributes', 'page-title', nodeContainerId)

sortTable = {
        'EE=' : 'no',
        'FF' : 'might',
        'FF=' : 'yes',
        'EF' : 'might',
        'FE' : 'yes'
}

i = 0
for row in rows:
        sort = ''
        auto = ''
        if i != 0:
                if row[1] == '':
                        sort += 'E'
                else:
                        sort += 'F'
                if row[2] == '':
                        sort += 'E'
                else:
                        sort += 'F'
                if row[1] == row[2]:
                        sort += '='
                row[3] = sort
                row[4] = sortTable[sort]
                row[5] = row[4]
        spamwriter.writerow(row)
        i += 1