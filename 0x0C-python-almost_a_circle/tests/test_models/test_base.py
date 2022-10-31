#!/usr/bin/python3
""" Modules to be test imported """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class Test_instances(unittest.TestCase):
    """ Test the instances created """

    def test_empty(self):
        """ Test no value passed """
        self.assertEqual(Base().id, Base().id - 1)

    def test_none(self):
        """ Test when none is passed """
        self.assertEqual(Base(None).id, Base(None).id - 1)

    def test_float(self):
        """ Test when float is passed """
        self.assertEqual(Base(3.1).id, 3.1)

    def test_str(self):
        """ Test when str is passed """
        self.assertEqual("Circle", Base("Circle").id)

    def test_list(self):
        """ Test when list is passed """
        self.assertEqual([1, 2, 3], Base([1, 2, 3,]).id)

class Test_to_json_string(unittest.TestCase):
    """ Test the method to_json_string """

    def test_none(self):
        """ Test when non passed """
        self.assertEqual("[]", Base.to_json_string(None))

    def test_empty(self):
        """ Test when empty is passed """
        self.assertEqual("[]", Base.to_json_string([]))

    def test_no_parameter(self):
        """ Test no parameter passed """
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_parameter(self):
        """ Test more parameters passed """
        with self.assertRaises(TypeError):
            Base.to_json_string([], 5)

    def test__dict__(self):
        """ Test for instances dict """
        self.assertEqual(str, type(Base.to_json_string([Rectangle(5, 5).to_dictionary()])))

class Test_save_to_file(unittest.TestCase):
    """ Test the method save_to_file """

    @classmethod
    def erase(self):
        """ Erase all files created """
        try:
            os.remove("Base.json")
        except:
            pass
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_none(self):
        """ Test for none """
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fil:
            self.assertEqual("[]", fil.read())

    def test_empty(self):
        """ Test for empty list """
        Square.save_to_file([])
        with open("Square.json") as fil:
            self.assertEqual("[]", fil.read())

    def test_no_para(self):
        """ Test for no parameters """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_class(self):
        """ Test using differint class to save another instance """
        rec = Rectangle(2, 4)
        Base.save_to_file(rec)
        with open("Base.json") as fil:
            self.assertTrue(len(fil.read()))

class Test_from_json_string(unittest.TestCase):
    """ Test for method from_json_string """

    def test_none(self):
        """ Test for none """
        self.assertEqual([], Base.from_json_string(None))

    def test_empty(self):
        """ Test for empty string """
        self.assertEqual([], Base.from_json_string("[]"))

    def test_more_para(self):
        """ Test for more parameters """
        with self.assertRaises(TypeError):
            Base.from_json_string([], 10)

    def test_no_para(self):
        """ Test for no parameter """
        with self.assertRaises(TypeError):
             Base.from_json_string()

    def test_from_json_dictR(self):
        """ Test for good arguments """
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2}]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

class Test_create(unittest.TestCase):
    """ Test for method create """

    def test_rec(self):
        """ Create new instance of rec """
        rec = Rectangle(10, 7, 2, 8)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertEqual("[Rectangle] (3) 2/8 - 10/7", str(rec))

    def test_seq(self):
        """ Create new instance of seq """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_isnotequal(self):
        """ Check equality """
        rec = Rectangle(10, 7, 2, 8)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertIsNot(rec, rec2)

class Test_load_from_file(unittest.TestCase):
    """ Test for method load_from_file """

    @classmethod
    def erase(self):
        """ Erase all json files  if they exist """
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_empty(self):
        """ Test for empty onjs """
        self.assertEqual([], Rectangle.load_from_file())

    def test_more_para(self):
        """ Test for more parameters """
        with self.assertRaises(TypeError):
            Base.load_from_file([], 10)

    def test_load_file__type_rec(self):
        """ Test for equality """
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in load))
