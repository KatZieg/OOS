#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

'''
Generator Funktionen:
liefern einen ITERATOR zurück, keinen einzelnen Wert oder eine endlos lange Liste,
sondern eine bestimmte Liste.
Besonders Sinn wenn man nicht weiß wann man die Liste verlassen will.
Bei jedem Aufruf von next wird ein neues Element erzeugt!
'''
'''
map: r = map(func, seq)
map wendet func auf alle Elemente von seq an und schreibt die Ergebnisse in eine neue Liste
'''
def fahrenheit(T):
    return ((9.0/5)*T + 32)

def celsius (T):
    return (5.0/9)*(T-32)
temp = (12, 32, -3, 22, 6)   #tupel

F = list(map(fahrenheit, temp))
C = list(map(celsius, F))

print(F)
print(C)

'''
filter(func, liste)
filtert die Ergebnisse aus der Liste, für die die Funktion true ist
'''

def t_warm(t):
    s_warm = filter(lambda x: x > 20, t)
    return s_warm

W = list(t_warm(temp))
print(W)