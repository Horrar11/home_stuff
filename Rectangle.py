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
        self.quad1Point = Point(origin.getX() + length,origin.getY() + width)
        self.quad2Point = Point(origin.getX(), origin.getY() + width)
        self.quad3Point = origin
        self.quad4Point = Point(origin.getX() + length,origin.getY())
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
Perimeter: %d

The 4 corners of this Rectangle are:
%s
%s
%s
%s""" % (self.x,self.y,self.length,self.width,self.area,self.perimeter, self.quad1Point,self.quad2Point,self.quad3Point,self.quad4Point)
