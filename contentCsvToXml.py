#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

# from lxml import etree
# from xml import etree
# import xml

# import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET

# users = etree.Element("users")
# user = etree.SubElement(users, "user")
# user.set("data-id", "101")
# nom = etree.SubElement(user, "nom")
# nom.text = "Zorro"
# metier = etree.SubElement(user, "metier")
# metier.text = "Danseur"
# # print(etree.tostring(users, pretty_print=True))
# print(etree.ElementTree.tostring(users))

# https://docs.python.org/3.5/library/xml.etree.elementtree.html#additional-resources
tree = ET.ElementTree()
tree.parse("index.xhtml")
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
    print(child[0].text)
print(root[1][0].text)
# root.tag.Element('coco')
# print(root.tag.Element('coco'))

a = ET.Element('a')
root.append(a)

b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

# tree.Element('aaaaaaa')

tree.write("index.xhtml")


tree2 = ET.ElementTree()
# root2 = tree2.getroot()
root2 = ET.fromstring('<html></html>')
# root2.append(a)
tree2.write("index2.xhtml")
# root = fromstring(xml_text)