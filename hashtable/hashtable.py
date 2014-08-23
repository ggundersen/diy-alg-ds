#!/usr/bin/env python

"""----------------------------------------------------------------------------
hashtable.py

A hash table is a data structure that implements an associative array, mapping
keys to values. A hash function efficiently generates indices from the keys
added to the hash table. When a hash function produces the same index from two
distinct keys, the event is called a "collision."

Hashing is a good example of a space-time tradeoff. With infinite space, we
could use each key as an index in a large array. This is prohibitive since the
number of possible keys is large. With infinite time, we could not worry about
collisions, hashing to the same index and sequentially searching.
----------------------------------------------------------------------------"""


class Hashtable:


    def __init__(self):
        """Initialize empty hashtable."""
        self.N = 0  # Number of key-value pairs in the hash table
        self.a = [[]]


    def _hash(self, val, mod):
        """Return hash code after ensuring it is positive and within range."""
        return abs(hash(val)) % mod


    def _resize(self, lim):
        """Resizes internal array."""
        temp = [[] for _ in range(lim)]
        for i, v in enumerate(self.a):
            chain = self.a[i]
            for tple in chain:
                self._put(temp, tple[0], tple[1], lim, True)
        self.a = temp


    def _put(self, lst, key, val, mod, is_copy=False):
        idx = self._hash(key, mod)
        chain = lst[idx]
        if len(chain) == 0:
            chain.append((key, val))
            if not is_copy:
                self.N += 1
        else:
            not_added = True
            for tple in chain:
                if tple[0] == key:
                    not_added = False
                    break
            if not_added:
                chain.append((key, val))
                if not is_copy:
                    self.N += 1


    def put(self, key, val):
        """Add val at index hashed from key. Return void."""
        if len(self.a) == self.N:
            self._resize(2 * self.N)
        self._put(self.a, key, val, len(self.a))


    def get(self, key):
        """Return value stored at the index of hashed key."""
        chain = self.a[self._hash(key, len(self.a))]
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
    print(ht.a)
    print(ht.get('foo'))
