#!/usr/bin/python3
""" Requuired modules for the testing imported """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_instances(unittest.TestCase):
    """ Test the instances of Rectangle created """

    def test_empty(self):
        """ Test for no parameters """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_instanceof(self):
        """ Test for inheritance """
        self.assertIsInstance(Rectangle(5, 5), Base)

    def test_w_S(self):
        """ Test the widtth attribue """
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_h_S(self):
        """ Test the height attr """
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_five_arg(self):
        """ Test for equality """
        rec = Rectangle(10, 7, 2, 8, 4)
        rec2 = Rectangle(4, 2, 1, 3, 7)
        self.assertNotEqual(rec.id, rec2.id)

    def test_six_arg(self):
        """ Test for more parameters """
        with self.assertRaises(TypeError):
            Rectangle(10, 7, 2, 8, 4, 1)

class Test_width(unittest.TestCase):
    """ Test for width functionality """

    def test_none(self):
        """ Test for none """
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(None, 10)

    def test_negative(self):
        """ Test for negative value """
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Rectangle(-5, 5)

class Test_height(unittest.TestCase):
    """ Test for height functionality """

    def test_none(self):
        """ Test for none """
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(10, None)

    def test_negative(self):
        """ Test for negative value """
        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            Rectangle(5, -5)
