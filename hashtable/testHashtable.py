#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock

from hashtable import Hashtable


class TestHashtable(unittest.TestCase):


    def setUp(self):
        self.ht = Hashtable()


    def test_put(self):
        self.assertEqual(self.ht._size(), 0)
        self.ht.put('foo', 100)
        self.assertEqual(self.ht._size(), 1)


    def test_put_multiple_types(self):
        self.ht.put('foo', 100)
        self.ht.put(5, 'bar')
        self.assertEqual(self.ht.get('foo'), 100)
        self.assertEqual(self.ht.get(5), 'bar')


    def test_put_raises_exception(self):
        self.assertRaises(TypeError, self.ht.put, [], 100)

    
    def test_put_overwrite(self):
        self.ht.put('foo', 100)
        self.ht.put('foo', 200)
        self.assertEqual(self.ht._size(), 1)
        val = self.ht.get('foo')
        self.assertEqual(val, 200)


    def test_put_resize(self):
        self.ht._resize = MagicMock()
        self.ht.put('foo', 100)
        self.ht.put('bar', 200)
        self.assertTrue(self.ht._resize.called)


    def test_get(self):
        self.ht.put('foo', 100)
        val = self.ht.get('foo')
        self.assertEqual(val, 100)


if __name__ == '__main__':
    unittest.main()
