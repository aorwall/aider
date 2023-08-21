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
        if self.tail:
            self.tail.succeeding = new_node
            new_node.previous = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None
        self.length -= 1
        return value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.length -= 1
        return value

    def unshift(self, value):
        new_node = Node(value)
        if self.head:
            self.head.previous = new_node
            new_node.succeeding = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def delete(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node.previous:
                    node.previous.succeeding = node.succeeding
                else:
                    self.head = node.succeeding
                if node.succeeding:
                    node.succeeding.previous = node.previous
                else:
                    self.tail = node.previous
                self.length -= 1
                return
            node = node.succeeding
        raise ValueError("Value not found")

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.succeeding
