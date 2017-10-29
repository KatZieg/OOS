#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

'''
anonyme Funktion: lambda
lambda Argumentenliste: Ausdruck
'''

f = lambda x: x*3+7
r = f(10)
print(r)

g = lambda x,y,z: (x-y)*z

#oder auch
def gg(x,y,z):
    return (x-y)*z

print(g(1,2,3))
print(gg(1,2,3))

print(g(3,4,6))

#ohne Referenzierung:
(lambda x, y, z: (x-y)*z)(2,4,6)
print((lambda x, y, z: (x-y)*z)(2,4,6))