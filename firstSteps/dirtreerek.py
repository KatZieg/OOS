#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import os, sys
import hashlib

def inputProcessing(x):
    try:
        if os.path.isdir(x):
            print("The name of the directory is: ", x)
            dirProcessing(x)

        if os.path.isfile(x):
            fileProcessing(x)

    except:
        if not os.path.exists(x):
            if os.path.isdir(x):
                print("This directory does not exist.")
            if os.path.isfile(x):
                print("This file does not exist.")
        if os.access(x,0):
                print("No rights.")
        else:
            print("Could not process your entry.")

    #finally:
        #print('Again..')

def fileProcessing(x):
    n = os.path.basename(x)
    h = hashlib.md5(x)
    h.digest()
    print("The filename is: ", n, " ,the md5 sum is:  ", h)

def dirProcessing(x):
    lst = os.listdir(x)
    for i in lst:
        j = os.path.join(x, i)
        inputProcessing(j)

if __name__ == '__main__':
    feed = input("Please enter the name of a directory or a file, please use the absolute path : ").encode('utf-8')
    inputProcessing(feed)
