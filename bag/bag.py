#!/usr/bin/env python

"""----------------------------------------------------------------------------
bag.py

A bag is a collection where order and removing items are not supported. A bag's
primary function is to be iterated over.
----------------------------------------------------------------------------"""


class Bag:


    def __init__(self):
        self.N = 0
        self.a = []

    
    def isEmpty(self):
        return self.N == 0


    def size(self):
        return self.N

    
    def add(self, item):
        self.N += 1
        self.a.append(item)


    def each(self, fn):
        for item in self.a:
            fn(item)
