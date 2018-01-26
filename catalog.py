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

fileName = "catalog-master-fr-du-site-BE"

fichier = fileName + ".xml"
csvFile = fileName + '.csv'
arbre = etree.parse(fichier)
csvfile = open(csvFile, 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter='§', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = []
rowTitles = ['PRODUCT ID', 'TYPE', 'fr_BE', 'nl_BE', 'nl_NL', 'SORT', 'TO TRANSLATE AUTO']
rows.append(rowTitles)

def appendRow(rows, productId, sousNode, master):
        productId = product.get(productId)
        row = [productId, sousNode, '', '', '', '', '']
        for node in master.iter(sousNode):
                lang = node.get('lang')
                if lang == 'fr-BE':
                        row[2] = node.text.strip()
                if lang == 'nl-BE':
                        row[3] = node.text.strip()
                if lang == 'nl-NL':
                        row[4] = node.text.strip()
        rows.append(row)

def appendCustomAttrToRow(rows, product,attrIdStr):
        for customAttributes in product.iter('custom-attributes'):
                productId = product.get('product-id')
                row = [productId, attrIdStr, '', '', '', '', '']
                for customAttribute in customAttributes.iter('custom-attribute'):
                        lang = customAttribute.get('lang')
                        attributeId = customAttribute.get('attribute-id')
                        if attributeId == attrIdStr:
                                if lang == 'fr-BE':
                                        row[2] = customAttribute.text.strip()
                                        # row.append(customAttribute.text.strip())
                                if lang == 'nl-BE':
                                        row[3] = customAttribute.text.strip()
                                        # row.append(customAttribute.text.strip())
                                if lang == 'nl-NL':
                                        row[4] = customAttribute.text.strip()
                                        # row.append(customAttribute.text.strip())
                rows.append(row)

customAttrNeeded = [
        'Accessories',
        'AccessoryDiameter',
        'AirBrushType',
        'AirDryerType',
        'AirFlow',
        'categoryAlias',
        'CutSystem',
        'descriptionSlotProduct',
        'DifferentsFeatures',
        'EpilationTechnical',
        'expertReview',
        'faqProduct',
        'FreedomOfMove',
        'HairType',
        'HeadType',
        'HeightOfCut',
        'Lighting',
        'longDescriptionLeft',
        'longDescriptionRight',
        'PowerSupply',
        'PrecisionAndAdjustment',
        'specialFeatures',
        'StraightenerType',
        'Sustainability'
]

sortTab = {
        'EEE==fr_&_==nl_NL':'NO',
        'EEF==fr_&_!=nl_NL':'YES',
        'EFE!=fr_BE_&_!=nl_NL':'MIGHT',
        'EFF!=fr_BE_&_!=nl_NL':'MUST',
        'EFF!=fr_BE_&_==nl_NL':'NO',
        'FEE!=fr_BE_&_==nl_NL':'YES',
        'FEF!=fr_BE_&_!=nl_NL':'YES',
        'FFE!=fr_BE_&_!=nl_NL':'MIGHT',
        'FFE==fr_&_!=nl_NL':'YES',
        'FFF!=fr_BE_&_!=nl_NL':'MIGHT',
        'FFF!=fr_BE_&_==nl_NL':'NO',
        'FFF==fr_&_!=nl_NL':'YES',
        'FFF==fr_&_==nl_NL':'YES'
}

for noeud in arbre.xpath('//catalog'):
        for product in noeud.iter('product'):
                appendRow(rows, 'product-id', 'display-name', product)
                appendRow(rows, 'product-id', 'long-description', product)
                appendRow(rows, 'product-id', 'short-description', product)
                for attrId in customAttrNeeded:
                        appendCustomAttrToRow(rows, product, attrId)
                # variation-attribute>display-name

for index in range(len(rows)):
        row = rows[index]
        if index == 0:
                spamwriter.writerow(row)
                continue

        sort = ''
        # full or empty FEE
        for i in range(3):
                if row[i + 2] != '':
                        sort += 'F'
                else:
                        sort += 'E'
        # nl_BE=fr_BE_and_nl_BE!=nl_NL
        cellFrBE = row[2]
        cellNlBE = row[3]
        cellNlNl = row[4]
        if cellNlBE == cellFrBE:
                sort += '==fr_&_'
        else:
                sort += '!=fr_BE_&_'
        if cellNlBE == cellNlNl:
                sort += '==nl_NL'
        else:
                sort += '!=nl_NL'
        row[5] = sort

        # EFE!=fr_BE_&_!=nl_NL
        row[6] = sortTab[sort]

        spamwriter.writerow(row)