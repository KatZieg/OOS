#!/usr/bin/python
# -*- coding: utf-8 -*-

#print('hello world')

a=0
b=1
if a<b :
    print('hello world')

import time
t = time.localtime()
h = t.tm_hour

if h<6:
    print('guten Morgen')
elif h<18 :
    print('hello')
else :
    print('good evening')

while h<18:
    print('bla')
    break

else :
    print('bla bla')

for i in "hallo":
    print(i)

def fname(a,b):
    a = a+1
    return a

def mult(a,b):
    return a*b

print(mult(3,4)) #position parameters
print(mult(a=23,b=2)) #named parameter, order dosent matter


for i in range (29):
    if i%3 == 0:
        print(i)
        if 1<i<7:
            print("Bingo!")
            print ("___")


#Folien Woche 2
#functions are objects

def func1(a,b):
    if test(a):
        return b
    return a

'''kommentare
weitere kommentare
'''

#help('keywords')
#help('POWER')
