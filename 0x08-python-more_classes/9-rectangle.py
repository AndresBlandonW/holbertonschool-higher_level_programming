#!/usr/bin/python3
"""Creates class that defines a rectangle"""


class Rectangle:
    """Create a rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width and check errors"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height and check errors"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Print the rectangle using (#)"""
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for i in range(self.__height):
            string += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """String Representation"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Delete class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        height = size
        width = size
        return cls(height, width)
