#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

def factorial(n):
    """
    >>> factorial(4)
    120 #sollte 24 sein
    >>> factorial(1)
    1
    """

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
