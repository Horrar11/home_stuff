#!usr/bin/python
from Cell import *
import math
import random
import cmd
import time

class Game(cmd.Cmd):
    print "\n" * 10
    global cellName
    prompt = raw_input("What is the name of this cell?") + ">"
    cellName = prompt
    global cell
    cell = Cell()
    def __init__(self):
        cmd.Cmd.__init__(self)
    def do_tick(self, args):
        cell.tick()
        if(cell.testDeath()):
            cell.__del__()
            del cell
        print cell
    def do_die(self, args):
        print "The cell died..."
        time.sleep(3)
        print "It will forever live on in the matrix..."
        time.sleep(3)
        exit()
if __name__ == "__main__":
    g = Game()
    g.cmdloop()
    
