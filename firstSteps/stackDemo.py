#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import stack #Modul Stack ist eingebunden
#import stack as Stapel
#from stack import Stack -> Vorteil: stack ist in Namensraum importiert worden
#from stack import * -> alles ist in Namensraum importiert

#s = Stapel.Stack()  -> alias Stapel wird verwendet

s = stack.Stack()
s.push(3)
print(s.pop())


if __name__ == '__main__':
    print(s)
    print(__file__)