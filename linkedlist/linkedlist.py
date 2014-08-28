#!/usr/bin/env python

"""----------------------------------------------------------------------------
linkedlist.py
----------------------------------------------------------------------------"""


class Linkedlist:
   
    class Node:

        def __init__(self, item, next=None, prev=None):
            """Initialize node with default 'pointer' to None."""
            self.item = item
            self.next = next
            self.prev = prev

    def __init__(self):
        """Initialize empty linked list."""
        self.first = None
        self.N = 0

    def is_empty(self):
        """Return true if list is empty, false otherwise."""
        return self.first == None

    def size(self):
        """Return number of nodes."""
        return self.N

    def add_first(self, item):
        """Add item to end of list."""
        if self.is_empty():
            self.first = self.Node(item)
        else:
            temp = self.first
            self.first = self.Node(item, temp)
            temp.prev = self.first
        self.N += 1

    def add_at(self, item, idx):
        """Add item at index. Zero-based index."""
        if self.is_empty():
            self.first = self.Node(item)
            return
        elif self.size() < idx:
            node = self.first
            while node and node.next:
                node = node.next
            new_node = self.Node(item, None, node)
            node.next = new_node
            return

        count = 0
        node = self.first
        while node and node.next and count < idx:
            node = node.next
            count += 1
        new_node = self.Node(item, node)
        node.prev.next = new_node

    def get_first(self):
        """Get first but do not remove from list."""
        if self.first:
            return self.first.item
        return None

    def get_at(self, idx):
        """Get at index but do not remove from list. Zero-based index."""
        if self.is_empty() or self.size() < idx:
            return None

        node = self.first
        count = 0
        while count < idx and node and node.next:
            node = node.next
            count += 1
        return node.item

    def remove_at(self, idx):
        if self.is_empty() or self.size() < idx:
            return None
        node = self.first
        count = 0
        while count < idx and node and node.next:
            node = node.next
            count += 1
        temp = node
        node.prev.next = node.next
        return temp.item

    def remove_first(self):
        """Remove first item from list."""
        if self.is_empty():
            return
        node = self.first
        self.first = self.first.next
        return node.item

    def _expose(self):
        node = self.first
        result = ''
        while node is not None:
            result += str(node.item) + '-'
            node = node.next
        return result[:-1]  # Remove trailing '-'

    def _pp(self):
        """Pretty print list."""
        count = 0
        node = self.first
        while node is not None:
            print(str(count) + ': ' + str(node.item))
            node = node.next
            count += 1
