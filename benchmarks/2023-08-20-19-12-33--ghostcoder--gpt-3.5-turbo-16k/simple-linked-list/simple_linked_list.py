class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._tail = None
        for value in values:
            self.push(value)

    def __len__(self):
        count = 0
        current = self._head
        while current:
            count += 1
            current = current.next()
        return count

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        if self._head is None:
            self._tail = None
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current = self._head
        while current:
            reversed_list.push(current.value())
            current = current.next()
        return reversed_list


class EmptyListException(Exception):
    pass