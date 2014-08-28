#!/usr/bin/env python

import unittest

from bag import Bag


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def test_is_empty(self):
        self.assertTrue(self.bag.is_empty())
        self.bag.add(3)
        self.assertTrue(not self.bag.is_empty())

    def test_size(self):
        self.assertEqual(self.bag.size(), 0)
        self.bag.add(3)
        self.assertEqual(self.bag.size(), 1)

    def test_add(self):
        self.bag.add(3)
        self.assertEqual(self.bag._a, [3])  # This code smells.

    def test_each(self):
        self.bag.add(3)
        self.bag.add('foo')
        self.bag.add([])
        lst = []
        self.bag.each(lambda x: lst.append(x))
        self.assertEqual([3, 'foo', []], lst)


if __name__ == '__main__':
    unittest.main()
