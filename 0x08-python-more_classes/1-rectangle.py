#!/usr/bin/python3
"""
This module contains

is_valid: Returns true if arguments are valid
"""


def is_valid(**kwargs):
    """ Returns true if arguments are integers """
    for arg in kwargs:
        if isinstance(kwargs[arg], int) != True:
            raise TypeError(f"{arg} must be an integer")
        if kwargs[arg] < 0:
            raise ValueError(f"{arg} must be >= 0")

    return True


class Rectangle:
    """ A Rectangle class """

    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle instance """

        if is_valid(width=width, height=height):
            self.__width = width
            self.__height = height


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, value):
        if is_valid(width=value):
            self.__width = value
    

    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, value):
        if is_valid(height=value):
            self.__height = value
