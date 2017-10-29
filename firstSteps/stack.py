#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

class Stack(object):
    '''docstring'''
    anz = 0

    def __init__(self):  #Constructor
        self.items = [] #Instance
        Stack.anz +=1

    def __del__(self):
        if Stack:
            Stack.anz -= 1 #self.anz wäre eine Instanzvariable!!

    def push(self,x): #etwas auf den Stack packen
        self.items.append(x)

    def pop(self): #etwas vom Stack nehmen, immer das letzte
        x = self.items[-1]
        del(self.items[-1])
        return x

    def __ichBinGeheim(self):
        print("das sollte man nie sehen")

    def _ichBinEinGeschutzt(self):
        print("ich bin geschützt")

    def __str__(self):
        return "Ich bin ein Stack der Länge {} mit den folgenden Elementen : {} und befinde mich in der {} Datei"\
            .format(len(self.items), self.items, __file__ )

    def __len__(self):
        return len(self.items)

if __name__ == '__main__':  #nur true, wenn das script direkt ausgeführt wird, nicht eingebunden
    s = Stack()
    s.push(34)
    #print(s.pop())
    #s.__ichBinGeheim() #geht nicht
    #s._ichBinEinGeschutzt()
    s1= Stack()
    print(len(s))
    #del(s)
    print(Stack.anz)
    print(s.items[-1])


