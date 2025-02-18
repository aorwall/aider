class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        if not values:
            values = []
        self._head = None
        for val in values:
            self.push(val)

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        length = 0
        current = self._head
        while current:
            length += 1
            current = current.next()
        return length

    def head(self):
        return self._head

    def push(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next():
                current = current.next()
            current._next = new_node

    def pop(self):
        if not self._head:
            raise EmptyListException("Cannot pop element from an empty list")
        popped_element = self._head.value()
        self._head = self._head.next()
        return popped_element

    def reversed(self):
        prev = None
        current = self._head
        while current:
            next_node = current.next()
            current._next = prev
            prev = current
            current = next_node
        self._head = prev


class EmptyListException(Exception):
    pass
