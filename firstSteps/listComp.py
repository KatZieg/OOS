#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

'''
List Comprehension
'''

l_eins = []

for i in range(1,10):
    l_eins.append(i*i)

print(l_eins)

#kurz und geschachtelt:
l_zwei = [i*i for i in range(1,11) if i%2 == 0]
print(l_zwei)

#keine Ausdrücke produzieren, die kein Mensch mehr versteht
l_drei = [(x,y) for x in range(3) for y in range(3) if x!=y]

print(l_drei)

#das gleiche mit runden Klammern:
g_drei = ((x,y) for x in range(3) for y in range(3) if x!=y)

#Adresse
print(g_drei)

#keine Unterschiede ob runde oder eckige Klammern!!!!
for i in g_drei:
    print(i)

for i in l_drei:
    print(i)

#dictionary comprehension
d_eins = {a: len(a) for a in ('Hello', 'World', 'am', 'Mittwoch')}

print(d_eins)