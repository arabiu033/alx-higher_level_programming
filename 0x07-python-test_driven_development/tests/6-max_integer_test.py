#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Use unittest to test max_integer function """
    def test_1(self):
        """ test for list of unmbes """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_2(self):
        """ test for empty list """
        self.assertEqual(max_integer([]), None)

    def test_3(self):
        """ test for negative lists """
        self.assertEqual(max_integer([-3, -5, -2, -1]), -1)
