#!/usr/bin/python3
"""Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init method for Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str method"""
        msg = "[Square] ({:d}) {:d}/{:d} - {:d}"
        msg = msg.format(self.id, self.x, self.y, self.width)
        return msg

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size and check errors"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns and arg with key to atributte"""
        my_list = [None, None, None, None]

        for i in range(len(args)):
            my_list[i] = args[i]

        if my_list[0] is not None:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if my_list[1] is not None:
            self.size = args[1]
        elif 'size' in kwargs:
            self.size = kwargs['size']
        if my_list[2] is not None:
            self.x = args[2]
        elif 'x' in kwargs:
            self.x = kwargs['x']
        if my_list[3] is not None:
            self.y = args[3]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """
        Return the dictionary representation
        of a Square
        """
        new_dict = {}

        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        new_dict['id'] = self.id

        return new_dict
