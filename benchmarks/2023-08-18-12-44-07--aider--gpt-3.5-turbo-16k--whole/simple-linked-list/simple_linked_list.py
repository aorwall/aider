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
        self._length = 0

        for value in values:
            self.push(value)

    def __len__(self):
        return self._length

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

        self._length += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        current = self._head
        previous = None

        while current._next is not None:
            previous = current
            current = current._next

        if previous is None:
            self._head = None
            self._tail = None
        else:
            previous._next = None
            self._tail = previous

        self._length -= 1

        return current

    def reversed(self):
        reversed_list = LinkedList()

        current = self._head

        while current is not None:
            reversed_list.push(current.value())
            current = current.next()

        return reversed_list


class EmptyListException(Exception):
    pass
