class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding  
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.succeeding
            
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.succeeding = None
        popped.previous = None
        popped.succeeding = None
        self.length -= 1
        return popped.value
        
    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        
    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        shifted = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.succeeding
            self.head.previous = None
        shifted.succeeding = None
        shifted.previous = None
        self.length -= 1
        return shifted.value
        
    def delete(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.succeeding = current.succeeding
                else:
                   