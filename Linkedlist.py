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

def SearchKey(self, key):
    """method to find the position of an element"""
    p = self.head #first node of the list
    index = 0 #indext corresponding to key
    # loop over all nodes in the linked list
    while p:
        #if element of node is key return index
        if p.element == key:
            return index
        #move p to next node and increment index
        else:
            p = p._next 
            index += 1
    return 'Element is not in the list'

def InsertFirstElement(self, e):

    #create a node with element e
    FirstNode = Node(e, None)
    #update the _next attribute with head object 
    if self.isempty():
        self.head = FirstNode
        self.tail = FirstNode
    else:
        FirstNode._next = self.head
        self.head = FirstNode
    self.size += 1
    
def InsertAnywhere(self, e, index):
    #creat a node with element e
    p = self.head
    ANode = Node(e, None)
    i = 1
    while i < index - 1:
        #go until you find the last element aftre which the given element needs to be inserted
        p = p._next
        i += 1
    ANode._next = p._next
    p._next = ANode
    self.size += 1
    
def insert_sorted(self,e):
    new_node = Node(e, None)
    if self.isempty():
        self.head = new_node
    else:
        p = self.head
        q = self.head
        while p and p.element<e:
            q = p
            p = p._next
        if p == self.head:
            new_node._next = self.head
            self.head = new_node
        else:
            new_node._next = q._next
            q._next = new_node
    self.size += 1
    
def DelStartElement(self):
    """Method to delete first element of a linked list"""
    
    if self.isempty():
        return 'list is empty'
    
    p = self.head
    e = p.element
    self.head = p._next #update head to second element in linked list
    self.size -= 1 #update size of linked list
    return f'{e} is deleted'
    if self.isempty():
        p.tail = None 
        
def DelEndElement(self):
    """Method to delete last element of a Linked List"""
    
    if self.isempty():
        return 'List is empty'
    elif self.size == 1: #if size of list is 1 then assign both head and tail as None 
        self.head = None
        self.tail = None
        self.size -= 1
    else: 
        e = self.tail.element #element to be deleted 
        p = self.head
        i = 1
        while i < self.size -1: #find the second last element 
            p = p._next
            i += 1
        p._next = None #assign _next attribute as None for second last element
        self.size -= 1
        self.tail = p
        return f'{e} is deleted'
    
def DelAnyElement(self, index):
    """Method to delete an element form location index"""
    
    if self.isempty():
        return "List is empty"
    else:
        p = self.head
        i = 1
        while i < index - 1:
            p = p._next
            i += 1
            
        e = p._next.element #element to be deleted
        p._next = p._next._next 
        self.size -= 1
        return f'{e} is deleted'


class LinkedList(Node):
    "Class to create linked list"
    
    #define a LinkedList with attributes as firt node (head), last node (tail), and size of linkedlist
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    #method to return the value of self.size (lenght of linked list)
    def __len__(self):
        return self.size
    
    #method to check if value of self.size is zero or not (list empty or not)
    def isempty(self):
        return self.size == 0
    
    #method to add nodes to linked list
    def addlast(self,e):
        newest = Node(e,None)
        if self.isempty(): #if list is empty add newest as the first node of LinkedList 
            self.head = newest
        else: #else add newest as a _next attribute to last node 
            self.tail._next = newest
        #update last node as the newest node
        self.tail = newest 
        self.size += 1
        
    #method to find the position of an element    
    SearchKey = SearchKey
    
    #method to insert an element at the beginning of a list
    InsertFirstElement = InsertFirstElement
    
    #method to insert element anywhere in the list
    InsertAnywhere = InsertAnywhere
    
    #method to delete first element from a Linked List
    DelStartElement = DelStartElement
    
    #method to delete last element from a linked list
    DelEndElement = DelEndElement
    
    #method to delet element from a specified position
    DelAnyElement = DelAnyElement
    
    #method to insert element in sorted order 
    insert_sorted = insert_sorted
    
    #method to display elements of nodes.
    def display(self):
        p = self.head
        while p:
            print(p.element, end = '  ')
            p = p._next
        print()
        
