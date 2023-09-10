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

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        current_node = self.tail
        if current_node.previous is None:
            self.head = None
        else:
            current_node.previous.succeeding = None
        self.tail = current_node.previous
        self.length -= 1
        return current_node.value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        current_node = self.head
        if current_node.succeeding is None:
            self.tail = None
        else:
            current_node.succeeding.previous = None
        self.head = current_node.succeeding
        self.length -= 1
        return current_node.value

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

    def __len__(self):
        return self.length

    def __iter__(self):
        current_node = self