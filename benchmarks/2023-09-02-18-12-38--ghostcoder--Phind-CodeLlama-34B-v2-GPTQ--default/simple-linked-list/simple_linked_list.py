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
        for value in values:
            self.push(value)

    def __len__(self):
        count = 0
        node = self._head
        while node:
            count += 1
            node = node.next()
        return count

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        else:
            return self._head.value()

    def push(self, value):
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        else:
            popped_value = self._head.value()
            self._head = self._head.next()
            return popped_value

    def reversed(self):
        prev_node = None
        current_node = self._head
        while current_node:
            next_node = current_node.next()
            current_node._next = prev_node
            prev_node = current_node
            current_node = next_node
        self._head = prev_node

    def __iter__(self):
        self._current_node = self._head
        return self

    def __next__(self):
        if self._current_node is not None:
            current_value = self._current_node.value()
            self._current_node = self._current_node.next()
            return current_value
        else:
            raise StopIteration


class EmptyListException(Exception):
    pass
