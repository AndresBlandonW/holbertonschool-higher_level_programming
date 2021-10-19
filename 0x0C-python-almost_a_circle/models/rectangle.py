#!/usr/bin/python3
"""Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method for Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width and check errors"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """Return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x and check errors"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y and check errors"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height and check errors"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    def area(self):
        """Return area"""
        return self.__height * self.__width

    def display(self):
        """Print rectangle with # and using x, y"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Str method"""
        m = "[Rectangle] ({}) {}/{} - {}/{}"
        m = m.format(self.id, self.__x, self.__y, self.__width, self.__height)
        return m

    def update(self, *args, **kwargs):
        """Assigns and arg with key to atributte"""
        my_list = [None, None, None, None, None]

        for i in range(len(args)):
            my_list[i] = args[i]

        if my_list[0] is not None:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if my_list[1] is not None:
            self.__width = args[1]
        elif 'width' in kwargs:
            self.__width = kwargs['width']
        if my_list[2] is not None:
            self.__height = args[2]
        elif 'height' in kwargs:
            self.__height = kwargs['height']
        if my_list[3] is not None:
            self.__x = args[3]
        elif 'x' in kwargs:
            self.__x = kwargs['x']
        if my_list[4] is not None:
            self.__y = args[4]
        elif 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """
        Return the dictionary representation
        of Rectangle
        """
        new_dict = {}

        for key in self.__dict__.keys():
            if 'width' in key:
                new_dict['width'] = self.__dict__[key]
            elif 'height' in key:
                new_dict['height'] = self.__dict__[key]
            elif 'x' in key:
                new_dict['x'] = self.__dict__[key]
            elif 'y' in key:
                new_dict['y'] = self.__dict__[key]
            elif 'id' in key:
                new_dict['id'] = self.__dict__[key]
        return new_dict
