#!usr/bin/python
from test import *

def test00():
    create02.__new__(Test())
    print create02.text
    create02.del()
