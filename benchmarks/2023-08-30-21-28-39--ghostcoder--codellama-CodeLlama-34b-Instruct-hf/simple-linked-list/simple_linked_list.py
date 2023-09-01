class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        self.size = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self.size

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.head is None:
            raise EmptyListException("The list is empty.")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def reversed(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


class EmptyListException(Exception):
    pass
