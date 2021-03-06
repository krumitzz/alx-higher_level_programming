#!/usr/bin/python3
"""
A simple square module
"""


class Square:
    """ A simpe square class """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        a = self.__size ** 2
        return a

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
