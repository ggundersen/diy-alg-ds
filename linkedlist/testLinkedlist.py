#!/usr/bin/env python

import unittest

from linkedlist import Linkedlist


class TestLinkedlist(unittest.TestCase):

    def setUp(self):
        self.ll = Linkedlist()

    def test_add_first(self):
        self.ll.add_first(3)
        self.ll.add_first(4)
        self.ll.add_first(99)
        self.assertEqual(self.ll._expose(),'99-4-3')

    def test_add_at(self):
        self.ll.add_first(3)
        self.ll.add_first(4)
        self.ll.add_first(99)
        self.ll.add_at(1, 1)
        self.assertEqual(self.ll._expose(),'99-1-4-3')

    def test_add_at_empty(self):
        self.ll.add_at(3, 9999)
        self.assertEqual(self.ll._expose(), '3')

    def test_add_at_big_index(self):
        self.ll.add_first(3)
        self.ll.add_first(4)
        self.ll.add_at(99, 9999)
        self.assertEqual(self.ll._expose(), '4-3-99')

    def test_get_first(self):
        self.ll.add_first(3)
        self.assertEqual(self.ll.get_first(), 3)

    def test_get_at(self):
        self.ll.add_first(3)
        self.ll.add_first(4)
        self.ll.add_first(99)
        self.assertEqual(self.ll.get_at(1), 4)

    def test_get_at_empty(self):
        self.assertEqual(self.ll.get_at(99), None)

    def test_get_at_big_index(self):
        self.ll.add_first(3)
        self.assertEqual(self.ll.get_at(99), None)

    def test_remove_first(self):
        self.ll.add_first(3)
        self.ll.add_first(4)
        item = self.ll.remove_first()
        self.assertEqual(item, 4)
        self.assertEqual(self.ll._expose(), '3')

    def test_remove_at(self):
        self.ll.add_first(3)
        self.ll.add_first(4)
        self.ll.add_first(99)
        val = self.ll.remove_at(1)
        self.assertEqual(val, 4)
        self.assertEqual(self.ll._expose(), '99-3')

    def test_remove_at_empty(self):
        self.assertEqual(self.ll.remove_at(99), None)

    def test_remove_at_big_index(self):
        self.ll.add_first(3)
        self.assertEqual(self.ll.remove_at(99), None)
        

if __name__ == '__main__':
    unittest.main()
