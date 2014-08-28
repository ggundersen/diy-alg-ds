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


if __name__ == '__main__':
    unittest.main()
