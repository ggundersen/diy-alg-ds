#!/usr/bin/env python

"""----------------------------------------------------------------------------
binarytree.py

A binary tree is a tree, the abstract data type, with a invariant that each
node has at most two child nodes. The root node is the only node in a tree
without a parent.
----------------------------------------------------------------------------"""

import pdb


class Binarytree:


    class Node:
        """Inner class to represent nodes in tree. Cannot be a namedtuple
        because this class is mutable."""
        
        def __init__(self, key, val, N):
            self.key = key
            self.val = val
            self.N = N
            self.left = None
            self.right = None


    def __init__(self):
        """Initialize empty binary tree."""
        self.root = None


    def _size(self, node):
        """Return size based on node's N property."""
        if node == None:
            return 0
        return node.N


    def size(self):
        """Delegate to private _size() to enable recursion."""
        return self._size(self.root)
        

    def _get(self, key):
        pass


    def get(self, key):
        """Get value based on key."""
        pass


    def _put(self, node, key, val):
        """Add key-value pair. Recursively return each subtree's root."""
        if node is None:
            return self.Node(key, val, 1)

        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val

        #pdb.set_trace()
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node


    def put(self, key, val):
        """Recursively delegate to private _put(). Return void."""
        self.root = self._put(self.root, key, val)


if __name__ == '__main__':
    bt = Binarytree()
    #pdb.set_trace()
    bt.put('foo', 100)
    bt.put('bar', 200)
    print( bt.size() )
