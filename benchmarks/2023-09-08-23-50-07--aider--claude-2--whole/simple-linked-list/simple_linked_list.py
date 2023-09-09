class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        return self.value

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        for value in values:
            self.push(value)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def head(self):
        if self.head is None:
            raise EmptyListException("List is empty")
        return self.head

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            raise EmptyListException("List is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def reversed(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.tail = self.head
        self.head = prev

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message
