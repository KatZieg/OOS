#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

'''
yield in Generator Funktionen:
durch yield werden die aktuelle Position und die darin enthaltenen Variablen gespeichert
und es erfolgt ein Rücksprung auf das aufrufende Programm mit dem hinter yield angegebenen Wert
bei jedem Schleifendurchlauf wird das jeweils nächste yield verwendet
Unterschied zu return: return ohne Rückgabewert beendet die Schleife
return mit Rückgabewert braucht einen Zähler
yield gibt einen Iterator zurück (wie Gernerator Expressions) also bei jedem Aufruf einen anderen Wert

'''

def range_generator(max):
    i = 0
    while i < max:
        yield i
        i += 1

for i in range_generator(10):
    print(i)

#generator mit mehreren yields
def generator_yields():
    a = 10
    yield a #erster Durchlauf a= 10
    yield a*2 #zweiter Durchlauf a=20
    b = 5
    yield a+b #dritter Durchlauf a=15

for i in generator_yields():
    print(i)

def enu(seq):
    n = 0
    for item in seq:
        yield n, item
        n += 1

generator = enu((3,1,5,7,2))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator)) #stop Iteration weil ausserhalb des Arrays

#liefert (0,3)-> erste Stelle 3, (1,1)->zweite Stelle 1