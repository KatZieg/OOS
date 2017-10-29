#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

class A(object):
    def foo(self, x):
        print("foo wird ausgeführt foo({},{}".format(self, x))

    @classmethod #Dekorator
    def cfoo(cls, x):
        print("foo wird ausgeführt foo({},{}".format(cls, x))

    @staticmethod
    def sfoo(x): #ohne self!
        print("foo wird ausgeführt foo ({})".format(x))

if __name__ == "__main__":
    A.cfoo('hallo') #Klasse auf Klasse ausführen nicht a Instanz
    A.sfoo('welt')

    a = A() #Instanziiert
    a.foo('normal') #auf Insatnz und Klasse zugreifen
    a.cfoo('class') #nur auf die Klasse
    a.sfoo('static') #auf gar nichts