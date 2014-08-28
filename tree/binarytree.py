#!/usr/bin/env python

"""----------------------------------------------------------------------------
binarytree.py

A binary tree is a tree, the abstract data type, with a invariant that each
node has at most two child nodes. The root node is the only node in a tree
without a parent.
----------------------------------------------------------------------------"""


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
        """Delegate to private _size() for recursion."""
        return self._size(self.root)

    def _get(self, node, key):
        """Return value based on key."""
        if node is None:
            return None

        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node

    def get(self, key):
        """Delegate to private _get() for recursion. Return val."""
        return self._get(self.root, key).val

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

        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def put(self, key, val):
        """Delegate to private _put() for recursion. Return void."""
        self.root = self._put(self.root, key, val)
