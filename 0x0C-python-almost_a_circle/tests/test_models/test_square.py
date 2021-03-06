#!/usr/bin/python3
"""Unittest Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquareClass(unittest.TestCase):
    """Test in Square class"""
    @classmethod
    def setUpClass(cls):
        """Setupclass unittest"""
        print('setupClass')

    def setUp(self):
        """SetUp unittest method"""
        print('setUp')
        self.squ1 = Square(5)
        self.squ2 = Square(2, 2)
        self.squ3 = Square(3, 1, 3)
        self.squ4 = Square(10, 2, 1)
        self.squ5 = Square(1, 1)

    def test_values(self):
        """Test for values in Init method"""
        # square 1 tests
        self.assertIsNotNone(self.squ1)
        self.assertIsInstance(self.squ1, Base)
        self.assertIsInstance(self.squ1, Rectangle)
        self.assertEqual(self.squ1.width, 5)
        self.assertEqual(self.squ1.height, 5)
        self.assertEqual(self.squ1.x, 0)
        self.assertEqual(self.squ1.y, 0)

        # square 2 tests
        self.assertIsNotNone(self.squ2)
        self.assertIsInstance(self.squ2, Base)
        self.assertIsInstance(self.squ2, Rectangle)
        self.assertIs(type(self.squ2), Square)
        self.assertEqual(self.squ2.width, 2)
        self.assertEqual(self.squ2.height, 2)
        self.assertEqual(self.squ2.x, 2)
        self.assertEqual(self.squ2.y, 0)

        # square 3 tests
        self.assertIsNotNone(self.squ3)
        self.assertIsInstance(self.squ3, Base)
        self.assertIsInstance(self.squ3, Rectangle)
        self.assertIs(type(self.squ3), Square)
        self.assertEqual(self.squ3.id, 90)
        self.assertEqual(self.squ3.width, 3)
        self.assertEqual(self.squ3.height, 3)
        self.assertEqual(self.squ3.x, 1)
        self.assertEqual(self.squ3.y, 3)

    def test_area(self):
        """Testing case for area method"""
        # square 1 tests
        self.assertEqual(self.squ1.area(), 25)

        # square 2 tests
        self.assertEqual(self.squ2.area(), 4)

        # square 3 tests
        self.assertEqual(self.squ3.area(), 9)

    def test_display(self):
        """Testing case for display method"""
        f = io.StringIO()
        with redirect_stdout(f):
            self.squ1.display()
        output = f.getvalue()
        self.assertEqual(output, f.getvalue())

    def test_str(self):
        """Testing case for __str__ method"""
        self.assertEqual(self.squ1.__str__(), "[Square] (68) 0/0 - 5")
        self.assertEqual(self.squ2.__str__(), "[Square] (69) 2/0 - 2")
        self.assertEqual(self.squ3.__str__(), "[Square] (70) 1/3 - 3")

    def test_update_args(self):
        """Testing case for update args method"""
        self.assertEqual(self.squ1.__str__(), "[Square] (78) 0/0 - 5")
        self.squ1.update(10)
        self.assertEqual(self.squ1.__str__(), "[Square] (10) 0/0 - 5")
        self.squ1.update(1, 2)
        self.assertEqual(self.squ1.__str__(), "[Square] (1) 0/0 - 2")
        self.squ1.update(1, 2, 3)
        self.assertEqual(self.squ1.__str__(), "[Square] (1) 3/0 - 2")
        self.squ1.update(1, 2, 3, 4)
        self.assertEqual(self.squ1.__str__(), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Testing case for update kwargs method"""
        self.squ1.update(x=12)
        self.assertEqual(self.squ1.__str__(), "[Square] (83) 12/0 - 5")
        self.squ1.update(size=7, y=1)
        self.assertEqual(self.squ1.__str__(), "[Square] (83) 12/1 - 7")
        self.squ1.update(size=7, id=89, y=1)
        self.assertEqual(self.squ1.__str__(), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """Testing case for to_dictionary method"""
        self.assertEqual(self.squ4.__str__(), "[Square] (76) 2/1 - 10")
        s4_dictionary = self.squ4.to_dictionary()
        expected = {'id': 76, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s4_dictionary, expected)
        self.assertIs(type(s4_dictionary), dict)

        self.assertEqual(self.squ5.__str__(), "[Square] (77) 1/0 - 1")
        self.squ5.update(**s4_dictionary)
        self.assertEqual(self.squ5.__str__(), "[Square] (76) 2/1 - 10")
        self.assertFalse(self.squ4 == self.squ5)

    def tearDown(self):
        """unittest tear down"""
        del self.squ1
        del self.squ2
        del self.squ3
        del self.squ4
        del self.squ5
        print("Processed...")
