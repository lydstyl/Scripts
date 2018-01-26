#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
Script de test
http://apprendre-python.com/page-xml-python-xpath
"""
# <?xml version="1.0" encoding="UTF-8"?>
# <users>
#     <user data-id="101">
#         <nom>Zorro</nom>
#         <metier>Danseur</metier>
#     </user>
#     <user data-id="102">
#         <nom>Hulk</nom>
#         <metier>Footballeur</metier>
#     </user>
#     <user data-id="103">
#         <nom>Zidane</nom>
#         <metier>Star</metier>
#     </user>
#     <user data-id="104">
#         <nom>Beans</nom>
#         <metier>Epicier</metier>
#     </user>
#     <user data-id="105">
#         <nom>Batman</nom>
#         <metier>Veterinaire</metier>
#     </user>
#     <user data-id="106">
#         <nom>Spiderman</nom>
#         <metier>Veterinaire</metier>
#     </user>
# </users>

from lxml import etree
# tree = etree.parse("test.xml")
tree = etree.parse("content-be-babyliss.xml")

# print(tree.xpath("/users/user/nom")[0].text)
# # print(tree.xpath("/users/user/nom")[1].text.tostring(users, pretty_print=True))
# print(etree.tostring(tree.xpath("/users/user/nom")[1], pretty_print=False))
# print(tree.xpath("/users/user/nom")[2].text)




# Voici un petit script qui affiche tous les noms des user.
# for user in tree.xpath("/users/user/nom"):
#     xmlstr = user.tostring(et, encoding='utf8', method='xml')

    # print(tostring(user, encoding='utf8', method='xml'))

# # Vous pouvez afficher les attributs des balises:
# for user in tree.xpath("/users/user"):
#     print(user.get("data-id"))

# # Vous pouvez affiner l'affichage en proposant de n'afficher que les user dont le métier est Veterinaire.
# for user in tree.xpath("/users/user[metier='Veterinaire']/nom"):
#     print(user.text)


# from lxml import etree
# tree = etree.parse("test.xml")
# # Voici un petit script qui affiche tous les noms des user.
# for user in tree.xpath("/users/user/nom"):
#     print(user.text)

# tree = etree.parse("test2.xml")
# for element in tree.xpath("/library/folder"):
#     print(element.get("folder-id"))




# 	si online-flag vaut true et <custom-attribute attribute-id="body" xml:lang="nl-BE">&lt;div class=
# 		imprimer les 

# import cgi

tree = etree.parse("content-be-babyliss.xml")
# i = 0
# onlineNb = 0
# for element in tree.xpath("/library/content"): # pour chaque content
#     online = tree.xpath("/library/content/online-flag")[i].text
#     if(online == 'true'):
#         print('y')
#         tree2 = etree.parse(element)
#     i += 1

#######test = etree.tostring(tree.xpath("/library/content/custom-attributes")[1], pretty_print=False)
test = etree.tostring(tree.xpath("/library/content/custom-attributes/custom-attribute")[0], pretty_print=False)
# print(tree.xpath("/library/content/custom-attributes/custom-attribute"))
for element in tree.xpath("/library/content"):
    print(element.get("content-id"))
    print(element.get("content-id"))
