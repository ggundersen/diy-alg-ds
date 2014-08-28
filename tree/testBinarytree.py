#!/usr/bin/env python

import unittest

from binarytree import Binarytree


class TestBinarytree(unittest.TestCase):

    def setUp(self):
        self.bt = Binarytree()

    def test_put(self):
        self.bt.put('foo', 3)
        self.assertEqual(self.bt.size(), 1)

    def test_put_more_than_once(self):
        self.bt.put('foo', 3)
        self.bt.put('bar', 99)
        self.bt.put('qux', 7)
        self.assertEqual(self.bt.size(), 3)

    def test_put_multiple_types_raises_error(self):
        self.bt.put('foo', 3)
        self.assertRaises(TypeError, self.bt.put, (5, 'baz'))

    def test_get(self):
        self.bt.put('foo', 3)
        self.assertEqual(self.bt.get('foo'), 3)

    def test_size(self):
        self.bt.put('foo', 3)
        self.assertEqual(self.bt.size(), 1)


if __name__ == '__main__':
    unittest.main()
