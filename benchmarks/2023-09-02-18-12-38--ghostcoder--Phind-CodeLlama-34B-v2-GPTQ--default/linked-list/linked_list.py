class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("List is empty")
        popped = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return popped

    def shift(self):
        if self._size == 0:
            raise IndexError("List is empty")
        shifted = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return shifted

    def unshift(self, value):
        node = Node(value, next=self.head)
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self._size += 1

    def __len__(self):
        return self._size

    def delete(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value and current_node == self.head:
                if not current_node.next:   # Only one node in the list
                    self.head = self.tail = None
                else:
                    next_node = current_node.next
                    current_node.next = None
                    next_node.prev = None
                    self.head = next_node
                self._size -= 1
                return True
            elif current_node.next and current_node.next.value == value:
                next_node = current_node.next
                current_node.next = next_node.next
                if next_node.next:
                    next_node.next.prev = current_node
                else:
                    self.tail = current_node
                self._size -= 1
                return True
            current_node = current_node.next
        raise ValueError("Value not found")
