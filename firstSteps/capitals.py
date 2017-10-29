#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'


COUNTRIES= (
    {'country':"United Staats", 'capital':"Washington"},
    {'country':"Germany", 'capital':"Berlin"},
    {'country':"France", 'capital':"Paris"},
    {'country':"Spain", 'capital':"Madrid", 'language':'Spanish'},
)

#print out the list of dictionaries

for country in COUNTRIES:
    print('The capital of {} is {}'. format(country['country'],
        country['capital']))
    if country.get('language'):  #.get wenn es den key nicht gibt keine Exception
        print('Und hier wird {} gesprochen'.format(country['language']))
