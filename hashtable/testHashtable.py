#!/usr/bin/env python

import unittest

from hashtable import Hashtable


class TestHashtable(unittest.TestCase):


    def setUp(self):
        self.ht = Hashtable()


    def test_put(self):
        self.assertEqual(self.ht._size(), 0)
        self.ht.put('foo', 100)
        self.assertEqual(self.ht._size(), 1)

    def test_get(self):
        self.ht.put('foo', 100)
        val = self.ht.get('foo')
        self.assertEqual(val, 100)


if __name__ == '__main__':
    unittest.main()
