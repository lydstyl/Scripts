#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Script de test
"""
filePath = '/home/lyd/Bureau/test.txt'

def rewriteSortedNoDuplicate(filePath):
        with open(filePath) as f:
                rows = f.readlines()
                rows = [x.strip() for x in rows]
                rows.sort()
                rows = list(set(rows))

                f = open(filePath, 'w')
                for row in rows:
                        f.write(row + "\n")

rewriteSortedNoDuplicate(filePath)