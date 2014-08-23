#!/usr/bin/env python

"""----------------------------------------------------------------------------
bag.py

A bag is a collection where order and removing items are not supported. A bag's
primary function is to be iterated over.
----------------------------------------------------------------------------"""


class Bag:


    def __init__(self):
        """Construct empty bag."""
        self.N = 0
        self.a = []

    
    def isEmpty(self):
        """Return true if the bag is empty, false otherwise."""
        return self.N == 0


    def size(self):
        """Return size of bag."""
        return self.N

    
    def add(self, item):
        """Add item of any type to bag."""
        self.N += 1
        self.a.append(item)


    # Is this functional style Pythonic?
    def each(self, fn):
        """Call fn on each item in the bag."""
        for item in self.a:
            fn(item)
