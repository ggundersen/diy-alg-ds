#!/usr/bin/env python

"""----------------------------------------------------------------------------
linkedlist.py
----------------------------------------------------------------------------"""


class Linkedlist:
   

    class Node:
        def __init__(self, item, next=None):
            """Initialize node with default 'pointer' to None."""
            self.item = None
            self.next = next

    
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
        """Add item as first."""
        if self.is_empty():
            self.first = Node(item)
        else:
            temp = self.first
            self.first = Node(item, temp)
        self.N += 1


    def remove_all(self, item):
        """Remove all nodes with item."""
        pass
