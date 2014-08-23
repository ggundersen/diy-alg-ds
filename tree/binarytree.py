#!/usr/bin/env python

"""----------------------------------------------------------------------------
binarytree.py

A binary tree is a tree, the abstract data type, with a invariant that each
node has at most two child nodes. The root node is the only node in a tree
without a parent.
----------------------------------------------------------------------------"""


class Binarytree:


    class Node:
        """Inner class to represent nodes in tree."""
        
        
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            self.N


    def __init__(self):
        """Initialize empty binary tree."""
        self.root = None


    def size(self):
        """Return size based on node's N property."""
        if self.root == None:
            return 0
        return self.root.N


    def _get(self, key):
        pass


    def get(self, key):
        """Get value based on key."""
        pass


    def _put(self, node, key, val):
        """Add key-value pair. Recursively return each subtree's root."""
        if node is None:
            return Node(key, val)
        # otherwise, go left or right...


    def put(self, key, val):
        """Recursively delegate to private _put(). Return void."""
        self.root = _put(self.root, key, val)
        
