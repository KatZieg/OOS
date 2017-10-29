#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

class Pizza(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size

Pizza.get_size(Pizza(42))