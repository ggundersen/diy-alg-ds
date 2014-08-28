#!/usr/bin/env python

"""----------------------------------------------------------------------------
bag.py

A bag is a collection where order and removing items are not supported. A bag's
primary function is to be iterated over.
----------------------------------------------------------------------------"""


class Bag:

    def __init__(self):
        """Construct empty bag."""
        self._N = 0
        self._a = []
    
    def is_empty(self):
        """Return true if the bag is empty, false otherwise."""
        return self._N == 0

    def size(self):
        """Return size of bag."""
        return self._N
    
    def add(self, item):
        """Add item of any type to bag."""
        self._N += 1
        self._a.append(item)

    # Is this functional style Pythonic?
    def each(self, fn):
        """Call fn on each item in the bag."""
        for item in self._a:
            fn(item)
