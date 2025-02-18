class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def push(self, value):
        new_node = Node(value, succeeding=self.head)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            self.head = new_node

        self._length += 1

    def pop(self):
        if not self.head:
            raise IndexError("List is empty")

        popped_value = self.head.value
        self.head = self.head.succeeding
        self._length -= 1

        return popped_value

    def shift(self):
        if not self.tail:
            raise IndexError("List is empty")

        shifted_value = self.tail.value
        self.tail = self.tail.previous
        self._length -= 1

        return shifted_value

    def unshift(self, value):
        new_node = Node(value, preceding=self.tail)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.succeeding = new_node
            self.tail = new_node

        self._length += 1

    def delete(self, value):
        current_node = self.head
        found = False

        while current_node:
            if current_node.value == value:
                found = True

                if current_node.previous:
                    current_node.previous.succeeding = current_node.succeeding
                else:
                    self.head = current_node.succeeding

                if current_node.succeeding:
                    current_node.succeeding.preceding = current_node.preceding
                else:
                    self.tail = current_node.preceding

                del current_node
                break

            current_node = current_node.succeeding

        if not found:
            raise ValueError("Value not found")

        self._length -= 1

    def __len__(self):
        return self._length

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.succeeding
