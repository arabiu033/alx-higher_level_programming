#!/usr/bin/python3
""" All required modules imported """
import unittest
from models.base import Base
from models.square import Square


class Test_instances(unittest.TestCase):
    """ Test the instances of square created """

    def test_empty(self):
        """ Test for no parameters """
        with self.assertRaises(TypeError):
            Square()

    def test_instanceof(self):
        """ Test for inheritance """
        self.assertIsInstance(Square(5), Base)

    def test_h_priv(self):
        """ Access private attr """
        with self.assertRaises(AttributeError):
            print(Square(10, 7, 8, 2).__size)

    def test_s_setter(self):
        """ Test for size functionality """
        sqr = Square(10, 7, 8, 2)
        sqr.size = 10
        self.assertEqual(10, sqr.size)

    def test_h_getter(self):
        """ Test for size functionality """
        sqr = Square(10, 7, 8, 2)
        sqr.size = 10
        self.assertEqual(10, sqr.height)

    def test_forequality(self):
        """ Test for equality """
        sqr = Square(10, 7, 2, 8)
        sqr2 = Square(4, 2, 1, 3)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_six_arg(self):
        """ Test for more parameters """
        with self.assertRaises(TypeError):
            Square(10, 7, 2, 8, 4, 1)

class Test_size(unittest.TestCase):
    """ Test for size functionality """

    def test_none(self):
        """ Test for none """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_negative(self):
        """ Test for negative value """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
