#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import stack
import unittest

class TestStack(unittest.TestCase):
    #wird vor jedem Testfall aufgerufen
    def setUp(self):
        self.s = stack.Stack()

    #wird nach jedem Testfall aufgerufen
    def tearDown(self):
        del(self.s)

    def test_1(self):
        self.s.push(3)
        x = self.s.pop()
        self.assertEqual(x, 3, msg='Da ging etwas schief')

    def test_2(self):
        self.s.push(3)
        self.s.push(4)
        x = self.s.pop()
        self.assertEqual(x, 4, msg='schief')
        x = self.s.pop()
        self.assertEqual(x, 3, msg='krumm')


    def test_3(self):
        self.assertRaises(Exception, self.s.pop, msg = 'das kann ich nicht vom Stack holen')


if __name__ == '__main__':
    unittest.main()