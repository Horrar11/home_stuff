#!usr/bin/python
from Point import *

class Rectangle:
    """"""
    def __init__(self, width = 0, length= 0, origin = Point(0,0)):
        """"""
        self.width = width
        self.length = length
        self.x = origin.getX()
        self.y = origin.getY()
        self.area = width * length
        self.perimeter = 2*(length+width)
    def getArea(self):
        return self.area
    def getPerimeter(self):
        return self.perimeter
    def getLocation(self):
        return "(%d,%d)" % (self.x,self.y)
    def __str__(self):
        return """ Properties of this Rectangle:
Origin Point: (%d,%d)
Length: %d
Width: %d
Area: %d
Perimeter: %d""" % (self.x,self.y,self.length,self.width,self.area,self.perimeter)
