#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import os
import hashlib

print(os.path.abspath(".")) #. relative Pfand zu aktuellem Skript
print(os.path) #Pfad zum Installationsmodul
print(os.path.basename(r"C:\Users\Kathi")) #gibt den Verzeichnisname zurück

print(os.path.dirname(r"C:\Users\Kathi\PycharmProjects\OOS\firstSteps\yield.py")) #gibt Pfad zur Datei zurück

print(os.path.exists(r"C:\Users\Kathi\PycharmProjects\OOS\firstSteps\yield.py")) #true

print(os.path.isdir(r"C:\Users\Kathi\PycharmProjects\OOS\firstSteps")) #Prüfung auf Verzeichnis

print(os.path.isfile(r"C:\Users\Kathi\PycharmProjects\OOS\firstSteps\yield.py")) #Prüfung auf Datei


print(hashlib.md5()) #object address


dirs = os.listdir(r"C:\Users\Kathi") #listet alle Inhalte auf
print(dirs)
for file in dirs: #gibt alle Verzeichnisse und Dateien aus
    print(file)
'''
gesuchtes_verzeichnis = input("Bitte ein gesuchtes Verzeichnis eingeben:")
print(os.path.isdir(gesuchtes_verzeichnis))
'''



