#!/usr/bin/env python

"""----------------------------------------------------------------------------
hashtable.py

A hash table is a data structure that implements an associative array, mapping
keys to values. A Hash function efficiently generates indexes from the keys
added to the hash table. When a hash function produces the same index from two
distinct keys, the event is called a "collision."

Hashing is a good example of a space-time tradeoff. With infinite space, we
could avoid all collisions. With infinite time, we could search sequentially.
----------------------------------------------------------------------------"""


class Hashtable:


    def __init__(self):
        """Initialize empty hashtable."""
        self.a = []


    def _hash(self, val):
        """Private hash function. For now, delegates to uilt-in hash()."""


    def _resize(self):
        """Doubles size of internal array."""
        pass


    def put(self, key, val):
        """Add val at index hashed from key. Return void."""
        pass


    def get(self, key):
        """Return value stored at the index of hashed key."""
        pass


if __name__ == 'main':
    ht = Hashtable()
