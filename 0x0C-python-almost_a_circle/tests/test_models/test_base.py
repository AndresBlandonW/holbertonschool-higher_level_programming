#!/usr/bin/python3
"""Unittest Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test Rectangle class"""
    def setUp(self):
        """SetUp unittest method"""
        self.base1 = Base()
        self.base2 = Base(3)
        self.rect1 = Rectangle(10, 7, 2, 8)
        self.rect2 = Rectangle(2, 4)
        self.squ1 = Square(5)
        self.squ2 = Square(7, 9, 1)

    def test_values(self):
        """Test for values in Init method"""
        # Base 1 tests
        self.assertIsNotNone(self.base1)
        self.assertIsInstance(self.base1, Base)
        self.assertEqual(self.base1.id, 32)

        # Base 2 tests
        self.assertIsNotNone(self.base2)
        self.assertIsInstance(self.base2, Base)
        self.assertEqual(self.base2.id, 3)

    def test_to_json_string(self):
        """Testing case for to_json_string method"""
        dictionary = self.rect1.to_dictionary()
        expected = {'x': 2, 'width': 10, 'id': 28, 'height': 7, 'y': 8}
        self.assertEqual(dictionary, expected)
        self.assertIs(type(dictionary), dict)
        json_string = Base.to_json_string([dictionary])
        output = '[{"x": 2, "width": 10, "id": 11, "height": 7, "y": 8}]'
        self.assertEqual(len(json_string), len(output))
        self.assertIs(type(json_string), str)

        empty_dict = None
        empty_str = Base.to_json_string(empty_dict)
        self.assertEqual(empty_str, "[]")

        empty_dict = []
        empty_str = Base.to_json_string(empty_dict)
        self.assertEqual(empty_str, "[]")

    def test_save_to_file(self):
        """Testing case for save_to_file method"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([self.rect1, self.rect2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 107)

    def test_from_json_string(self):
        """Testing case for from_json_string method"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIs(type(list_output), list)
        self.assertEqual(len(list_output[0]), len(list_input[0]))
        self.assertEqual(len(list_output[1]), len(list_input[1]))

    def test_create(self):
        """Testing case for create method"""
        self.rect3 = Rectangle(3, 5, 1)
        self.assertEqual(self.rect3.__str__(), '[Rectangle] (6) 1/0 - 3/5')
        r3_dictionary = self.rect3.to_dictionary()
        self.rect4 = Rectangle.create(**r3_dictionary)
        self.assertEqual(self.rect3.__str__(), '[Rectangle] (6) 1/0 - 3/5')

        self.assertFalse(self.rect3 is self.rect4)
        self.assertFalse(self.rect3 == self.rect4)

    def test_load_from_file(self):
        """Testing case for load_from_file method"""
        list_rectangles_input = [self.rect1, self.rect2]

        Rectangle.save_to_file(list_rectangles_input)

        r_output = Rectangle.load_from_file()
        self.assertEqual(self.rect1.__str__(), r_output[0].__str__())
        self.assertEqual(self.rect2.__str__(), r_output[1].__str__())
        self.assertFalse(self.rect1 is r_output[0])

        list_squares_input = [self.squ1, self.squ2]

        Square.save_to_file(list_squares_input)
        s_output = Square.load_from_file()
        self.assertEqual(self.squ1.__str__(), s_output[0].__str__())
        self.assertEqual(self.squ2.__str__(), s_output[1].__str__())
        self.assertFalse(self.squ1 is s_output[0])

    def tearDown(self):
        """unittest tear down"""
        print("Processed...")
