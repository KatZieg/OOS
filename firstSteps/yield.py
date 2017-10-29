#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

'''
yield in Generator Funktionen:
durch yield werden die aktuelle Position und die darin enthaltenen Variablen gespeichert
und es erfolgt ein Rücksprung auf das aufrufende Programm mit dem hinter yield angegebenen Wert
Unterschied zu rerun:

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
    yield a
    yield a*2
    b = 5
    yield a+b

for i in generator_yields():
    print(i)