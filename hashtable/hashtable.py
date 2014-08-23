#!/usr/bin/env python

"""----------------------------------------------------------------------------
hashtable.py implements a simple hash table.

A hash table is a data structure that implements an associative array, mapping
keys to values. A hash function efficiently generates indices from the keys
added to the hash table. When a hash function produces the same index from two
distinct keys, the event is called a "collision."

Hashing is a good example of a space-time tradeoff. With infinite space, we
could use the key as an index in a large array. This is prohibitive since the
number of possible key

Optimizations:
- Resize the array. Currently, this is not possible because the hash function's
  modulus is the length of the array. The hashed index would change whenever
  the array is resized.
- Pick a prime modulus.
----------------------------------------------------------------------------"""

import pdb


class Hashtable:


    def __init__(self):
        """Initialize empty hashtable."""
        self.N = 0  # Number of key-value pairs in the hash table
        self.a = [[]] * 10000  # TODO: Resize the hash table


    def _hash(self, val):
        """Return hash code after ensuring it is positive and within range."""
        return abs(hash(val)) % len(self.a)


    #def _resize(self, lim):
    #    """Resizes internal array."""
    #    temp = [[]] * lim
    #    for i, v in enumerate(self.a):
    #        temp[i] = self.a[i]
    #    self.a = temp


    def put(self, key, val):
        """Add val at index hashed from key. Return void."""
        #if len(self.a) == self.N:
        #    self._resize(2 * self.N)

        idx = self._hash(key)
        chain = self.a[idx]
        if len(chain) == 0:
            chain.append((key, val))
            self.N += 1
        else:
            not_added = True
            for tple in chain:
                if tple[0] == key:
                    not_added = False
                    break
            if not_added:
                chain.append((key, val))
                self.N += 1


    def get(self, key):
        """Return value stored at the index of hashed key."""
        chain = self.a[self._hash(key)]
        for tple in chain:
            if tple[0] == key:
                return tple[1]
        return None


if __name__ == '__main__':
    ht = Hashtable()
    ht.put('foo', 1000)
    ht.put('bar', 2000)
    ht.put('baz', 3000)
    ht.put('qux', 4000)
    print(ht.get('foo'))
