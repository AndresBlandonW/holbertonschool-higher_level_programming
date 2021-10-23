#!/usr/bin/python3
"""Unittest Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout


class TestRectangleClass(unittest.TestCase):
    """Test Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """Setupclass unittest"""
        print('setup unittest class')

    def setUp(self):
        """SetUp unittest method"""
        print("setUp")
        self.rect1 = Rectangle(3, 2)
        self.rect2 = Rectangle(5, 12, 3)
        self.rect3 = Rectangle(2, 10, 1, 1)
        self.rect4 = Rectangle(8, 7, 0, 0, 12)

    def test_values(self):
        """Test for values in Init method"""
        # Rectangle 1 tests
        self.assertIsNotNone(self.rect1)
        self.assertEqual(self.rect1.width, 3)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)
        self.assertIsInstance(self.rect1, Base)

        # Rectangle 2 tests
        self.assertIsNotNone(self.rect2)
        self.assertEqual(self.rect2.width, 5)
        self.assertEqual(self.rect2.height, 12)
        self.assertEqual(self.rect2.x, 3)
        self.assertEqual(self.rect2.y, 0)
        self.assertIsInstance(self.rect2, Base)

        # Rectangle 3 tests
        self.assertIsNotNone(self.rect3)
        self.assertEqual(self.rect3.width, 2)
        self.assertEqual(self.rect3.height, 10)
        self.assertEqual(self.rect3.x, 1)
        self.assertEqual(self.rect3.y, 1)
        self.assertIsInstance(self.rect3, Base)

        # Rectangle 4 tests
        self.assertIsNotNone(self.rect4)
        self.assertEqual(self.rect4.width, 8)
        self.assertEqual(self.rect4.height, 7)
        self.assertEqual(self.rect4.x, 0)
        self.assertEqual(self.rect4.y, 0)
        self.assertEqual(self.rect4.id, 12)
        self.assertIsInstance(self.rect4, Base)

    def test_area(self):
        """Testing case for area"""
        # Rectangle 1 tests
        self.assertEqual(self.rect1.area(), 6)

        # Rectangle 2 tests
        self.assertEqual(self.rect2.area(), 60)

        # Rectangle 3 tests
        self.assertEqual(self.rect3.area(), 20)

        # Rectangle 4 tests
        self.assertEqual(self.rect4.area(), 56)

    def test_display(self):
        """Testing case for display"""
        # Rectangle 1 tests
        f = io.StringIO()
        with redirect_stdout(f):
            self.rect1.display()
        output = f.getvalue()
        self.assertEqual(output, f.getvalue())

        # Rectangle 4 tests
        f = io.StringIO()
        with redirect_stdout(f):
            self.rect4.display()
        output = f.getvalue()
        self.assertEqual(output, f.getvalue())

    def test_str_(self):
        """Testing case __str__"""
        # Test with Rectangle 4
        self.assertEqual(str(self.rect4), "[Rectangle] (12) 0/0 - 8/7")

    def test_update_args(self):
        """Testing for update method with args"""
        self.assertEqual(self.rect1.__str__(), "[Rectangle] (49) 0/0 - 3/2")
        self.rect1.update(89)
        self.assertEqual(self.rect1.__str__(), "[Rectangle] (89) 0/0 - 3/2")

    def test_update_kwargs(self):
        """Testing for update method with kwargs"""
        self.assertEqual(self.rect1.__str__(), "[Rectangle] (52) 0/0 - 3/2")
        self.rect1.update(height=1)
        self.assertEqual(self.rect1.__str__(), "[Rectangle] (52) 0/0 - 3/1")
        self.rect1.update(x=1, height=5, y=3, width=7, id=89)
        self.assertEqual(self.rect1.__str__(), "[Rectangle] (89) 1/3 - 7/5")

    def test_to_dictionary(self):
        """Testing for to_dictionary method"""
        # Test with Rectangle 3
        self.assertEqual(self.rect3.__str__(), "[Rectangle] (48) 1/1 - 2/10")
        rect3_dictionary = self.rect3.to_dictionary()
        expected = {'x': 1, 'y': 1, 'id': 48, 'height': 10, 'width': 2}
        self.assertEqual(rect3_dictionary, expected)
        self.assertIs(type(rect3_dictionary), dict)

    def tearDown(self):
        """unittest tear down"""
        print("Processed...")
