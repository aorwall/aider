class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value


    @property
    def next(self):
        return self._next


    @next.setter
    def next(self, node):
        if not isinstance(node, (type(None), Node):
            raise TypeError("Next must be a Node object or None")
        self._next = node



class LinkedList:
    def __init__(self, values=None):
        self._head = None
        if values is not None:
            for val in values:
                self.push(val)


    def __len__(self):
        length = 0
        current = self._head
        while current is not None:
            length += 1
            current = current.next
        return length


    def head(self):
        if self._head is None:
            raise EmptyListException("Cannot get head of empty list")
        return self._head.value


    def push(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self):
        if self._head is None:
            raise EmptyListException("Cannot pop from empty list")
        popped_value = self._head.value
        self._head = self._head.next
        return popped_value


    def reversed(self):
        prev = None
        current = self._head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self._head = prev


class EmptyListException(Exception):
    pass
