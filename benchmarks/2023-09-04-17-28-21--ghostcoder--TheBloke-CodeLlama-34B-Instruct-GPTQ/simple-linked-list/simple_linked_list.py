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
        self._size = 0
        for v in values:
            self.push(v)

    def __len__(self):
        return self._size

    def head(self):
        return self._head

    def push(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise EmptyListException("Cannot pop from an empty list")
        elif self._size == 1:
            popped = self._head.value()
            self._head = None
            self._size -= 1
            return popped
        else:
            previous = None
            current = self._head
            while current.next is not None:
                previous = current
                current = current.next
            popped = current.value()
            previous.next = None
            self._size -= 1
            return popped

    def reversed(self):
        new_list = LinkedList()
        current = self._head
        while current:
            new_list.push(current.value())
            current = current.next
        return new_list


class EmptyListException(Exception):
    pass
