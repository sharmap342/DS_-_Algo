#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    """Class to create a node"""
    #The special attribute __slots__ allows you to explicitly state which instance attributes you 
    #expect your object instances to have, with the expected results: faster attribute access and space
    #savings in memory.
    #This is done by storing value references in __slots__ instead of __dict__
    #Denying __dict__ and __weakref__ creation if parent classes deny them and you declare __slots__
    __slot__ = 'element', '_next'
    
    #create a node with two attributes - element as value and _next as memory address for next element
    def __init__(self, element, _next):
        self.element = element
        self._next = _next

class QueueLink:
    """A class to implement queue using linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    #method to return length of queue
    def __len__(self):
        return self.size
    
    #method to check if queue is empty
    def isempty(self):
        return self.size == 0
    
    #method to insert element
    def enqueue(self, e):
        new_node = Node(e, None)
        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail._next = new_node
            self.tail = new_node
        self.size += 1
        
    #method to remove and return first element
    def dequeue(self):
        p = self.head
        if self.isempty():
            return "Queue is empty"
        else:
            el = self.head.element
            self.head = self.head._next
            self.size -= 1
            return el
        
    #method to retrun first element 
    def first(self):
        if self.isempty():
            return 'Queue is empty'
        else: 
            return self.head.element
        
    #method to display elements of queue
    def display(self):
        p = self.head
        while p:
            print(p.element, end='  ')
            p = p._next

