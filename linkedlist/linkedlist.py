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
        self.last = None
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
            self.first = self.Node(item, self.last)
        else:
            temp = self.first
            self.first = self.Node(item, temp)
            temp.prev = self.first
        self.N += 1

    def add_at(self, item, idx):
        """Add item at index."""
        if self.is_empty():
            self.first = self.Node(item, self.last)
            return
        elif self.size() < idx:
            self.last = self.Node(item, None, self.last) 
            return

        count = 0
        node = self.first
        while node and node.next and count < idx:
            node = node.next
            count += 1
        new_node = self.Node(item, node, node.prev)
        node.prev.next = new_node

    def get(self, idx):
        """Get but do not remove item from list."""
        if self.is_empty():
            return None

        node = self.first
        count = 1
        while count < idx and node and node.next:
            node = node.next
            count += 1
        return node.item

    def get_first(self, item):
        """Get but do not remove first item from list."""
        result = self.first
        if self.first.next is not None:
            self.first = self.first.next
        return result

    def remove_first(self):
        """Remove first item from list."""
        if self.is_empty():
            return
        self.first = self.first.next

    def pp(self):
        """Pretty print list."""
        count = 0
        node = self.first
        while node is not None:
            print(str(count) + ': ' + str(node.item))
            node = node.next
            count += 1


if __name__ == '__main__':
    ll = Linkedlist()
    ll.add_first('foo')
    ll.add_first('bar')
    ll.add_first('bop')
    ll.add_first('quz')
    ll.add_first('ili')
    ll.pp()
    print(ll.get(3))
    #ll.add_at('baz', 1)
    #ll.pp()

