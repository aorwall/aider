class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, value):
        new_node = Node(value, self.head)

        if self.head is not None:
            self.head.previous = new_node

        else:
            self.tail = new_node

        self.head = new_node
        self._size += 1

    def pop(self):
        if self.head is None:
            raise IndexError('List is empty')

        popped_node = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.previous = None

        else:
            self.tail = None

        self._size -= 1
        return popped_node.value

    def shift(self):
        if self.head is None:
            raise IndexError('List is empty')

        old_head = self.head
        self.head = old_head.next

        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None

        self._size -= 1
        return old_head.value

    def unshift(self, value):
        new_node = Node(value, self.head)

        if self.head is not None:
            self.head.previous = new_node
        else:
            self.tail = new_node

        self.head = new_node
        self._size += 1

    def delete(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                if current_node.previous is not None:
                    current_node.previous.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next is not None:
                    current_node.next.previous = current_node.previous
                else:
                    self.tail = current_node.previous

                self._size -= 1
                return True
            current_node = current_node.next

        raise ValueError('Value not found')

    def __len__(self):
        return self._size

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next
