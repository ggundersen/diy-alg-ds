#!/usr/bin/env python

"""----------------------------------------------------------------------------
linkedlist.py
----------------------------------------------------------------------------"""


class Linkedlist:
   

    class Node:
        def __init__(self, item, next=None):
            self.item = None
            self.next = next

    
    def __init__(self):
        self.first = None
        self.N = 0


    def is_empty(self):
        return self.N != 0


    def size(self):
        return self.N


    def add(self, item):
        if self.first == None:
            self.first = Node(item)
        else:
            self._add(self.first, item)
        
        #else:
        #    temp = self.first
        #    self.first = Node(item, temp)
        #self.N += 1


    def remove(self):
        pass
