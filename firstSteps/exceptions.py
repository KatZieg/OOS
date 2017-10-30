#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

lst = [1, 2, 3, 'jj', 0]

def demo(lst, i):
    try:
        x = 1.0/lst[i]
    except (IndexError, ZeroDivisionError):
        print('1, Exeption', i)
        return None
    except TypeError as e:
        print("Error: ", e.message)
        return None
    except: #any other
        pass
    else: #no exception
        return x
    finally:
        print('always executed')

for i in range(len(lst)+1):
    demo(lst,i)