#!/usr/bin/env python

"""----------------------------------------------------------------------------
hashtable.py

A hash table is a data structure that implements an associative array, mapping
keys to values. A Hash function efficiently generates indexes from the keys
added to the hash table. When a hash function produces the same index from two
distinct keys, the event is called a "collision."

Hashing is a good example of a space-time tradeoff. With infinite space, we
could avoid all collisions. With infinite time, we could search sequentially.

This hash table relies on linear probing for collision resolution.
----------------------------------------------------------------------------"""

import pdb


class Hashtable:


    def __init__(self):
        """Initialize empty hashtable."""
        self.N = 0   # Number of key-value pairs in the table
        self.M = 16  # Size of linear probing table; M > N
        self.a = [None] * self.M


    def _hash(self, val):
        """Return hash code after ensuring it is positive and within range."""
        return abs(hash(val)) % self.M


    def _resize(self, lim):
        """Doubles size of internal array."""
        temp = [None] * lim
        for i, v in enumerate(self.a):
            temp[i] = self.a[i]
        self.a = temp


    def put(self, key, val):
        """Add val at index hashed from key. Return void."""
        if self.N >= self.M / 2:
            self._resize(2 * self.M)
        # TODO: Deal with collisions
        self.a[self._hash(key)] = val
        self.N += 1


    def get(self, key):
        """Return value stored at the index of hashed key."""
        return self.a[self._hash(key)]


if __name__ == '__main__':
    ht = Hashtable()
    ht.put('foo', 1000)
    print(ht.get('foo'))
