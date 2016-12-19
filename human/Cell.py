#!usr/bin/python
import math
import random

constant = 1.0/671 * 100
class Cell:
    """This is a Cell: the most basic living thing.
I will be using Cells to try and construct a human."""
    def __init__(self, atp = random.randint(256,512), o2 = random.randrange(80,90,1)):
        self.atp = atp
        self.o2 = o2
        self.co2 = 100 - o2
        self.h2o = 90
    def __del__(self):
        print"The cell has died"
    def __str__(self):
        return """This is a cell with %d atp, %d of o2, %d of co2, and %d of h2o""" % (self.atp, self.o2, self.co2, self.h2o)
    def makeEnergy(self):
        self.atp += 2
        if(self.o2 > 80.0):
            self.atp += 34
            self.co2 += constant/2
            self.h2o -= constant/4
        self.o2 -= constant
        self.co2 += constant
        self.h2o -= constant/8
    def exist(self):
        self.atp -= 20
        self.o2 -= constant
        self.co2 += constant
        self.h2o -= constant/2
    def testDeath(self):
        if(self.o2 < 30.0):
            return True
        if(self.atp < 20):
            return True
        if(self.co2 > 60.0):
            return True
        if(self.h2o < 60.0):
            return True
        if(self.h2o > 99.0):
            return True
    def tick(self):
        self.exist()
        self.makeEnergy()
        self.testDeath()
