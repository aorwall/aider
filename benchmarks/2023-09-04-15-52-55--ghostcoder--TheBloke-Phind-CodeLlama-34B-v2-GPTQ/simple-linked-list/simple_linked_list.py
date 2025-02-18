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
        if values is None:
            values = []
        self._head = None
        for v in values[::-1]:  # Reversed so we can build the list efficiently
            self.push(v)

    def __len__(self):
        count = 0
        node = self._head
        while node is not None:
            count += 1
            node = node.next()
        return count

    def head(self):
        return self._head.value() if self._head else None

    def push(self, value):
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        removed_node = self._head
        self._head = self._head.next()
        return removed_node.value()

    def reversed(self):
        prev_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.next()
            current_node._next = prev_node
            prev_node = current_node
            current_node = next_node
        self._head = prev_node


class EmptyListException(Exception):
    def __init__(self, message):
        super().__init__(message)
