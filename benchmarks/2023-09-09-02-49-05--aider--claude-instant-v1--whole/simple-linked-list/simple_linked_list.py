class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        if values:
            node = Node(values[0])
            self.head = node
            current = self.head
            for value in values[1:]:
                current.next = Node(value)
                current = current.next

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.get_next()
        return count

    def get_head(self):
        return self.head

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            raise EmptyListException("The list is empty.")
        node = self.head
        if self.head.get_next() is None:
            self.head = None
            return node.get_value()
        while node.get_next().get_next():
            node = node.get_next()
        removed = node.get_next()
        node.next = None
        return removed.get_value()

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.get_next()

    def reversed(self):
        prev = None
        current = self.head
        while current:
            next_node = current.get_next()
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
