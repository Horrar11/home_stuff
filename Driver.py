#!usr/bin/python
from Rectangle import *

def testRect():
    rect00 = Rectangle()
    rect01 = Rectangle(6, 8, Point(5,5))
    print rect00
    print rect01
    print rect01.getArea()
    print rect01.getPerimeter()
    print rect01.getLocation()
testRect()
