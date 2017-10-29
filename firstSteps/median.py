#!/usr/bin/python
# -*- coding: utf-8 -*-


print('Median')
#chaining der operatoren

def median(a,b,c) :

    if a<b<=c or a>b>=c :
        return b
    if b<a<=c or b>a>=c :
        return a
    return c

print(median(11,319,21))

def middle(x,y,z) :
    return sorted([x,y,z])[1]

print(middle(11,310,21))

def mitte(a) :
    temp = sorted(a)
    return temp[int(len(temp)/2)]

print(mitte([11,310,21]))
