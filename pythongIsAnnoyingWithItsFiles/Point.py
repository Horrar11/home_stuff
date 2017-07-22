#!usr/bin/python
import math

class Point:
    """This is a point class. Creates a new point at (0,0) by default."""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def distanceTo(self, other):
        return (((self.x - other.x)** 2) + ((self.y - other.y)** 2)) ** 0.5
    def midpoint(self, other):
        mx = (self.x + other.x) / 2.0
        my = (self.y + other.y) / 2.0
        return Point(mx,my)
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
