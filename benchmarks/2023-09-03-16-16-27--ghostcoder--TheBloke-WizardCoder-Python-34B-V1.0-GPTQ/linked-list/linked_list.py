class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0


    def append(self, value):
        if not self._head:
            node = Node(value)
            self._head = node
            self._tail = node
        else:
            new_node = Node(value, self._tail)
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1


    def prepend(self, value):
        if not self._head:
            node = Node(value)
            self._head = node
            self._tail = node
        else:
            new_node = Node(value, self._head)
            self._head.prev = new_node
            self._head = new_node
        self._length += 1


    def delete(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        elif index == 0:
            old_head = self._head
            self._head = old_head.next
            if self._head:
                self._head.prev = None
            else:
                self._tail = None
            del old_head
            self._length -= 1
        elif index == self._length - 1:
            old_tail = self._tail
            self._tail = old_tail.prev
            self._tail.next = None
            del old_tail
            self._length -= 1
        else:
            current_index = 0
            current_node = self._head
            while current_index != index:
                current_node = current_node.next
                current_index += 1
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            del current_node
            self._length -= 1


    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        elif index == 0:
            return self._head.value
        elif index == self._length - 1:
            return self._tail.value
        else:
            current_index = 0
            current_node = self._head
            while current_index != index:
                current_node = current_node.next
                current_index += 1
            return current_node.value


    def insert(self, index, value):
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")
        elif index == 0:
            self.prepend(value)
        elif index == self._length:
            self.append(value)
        else:
            current_index = 0
            current_node = self._head
            while current_index != index - 1:
                current_node = current_node.next
                current_index += 1
            new_node = Node(value, current_node.next, current_node)
            current_node.next = new_node
            new_node.next.prev = new_node
            self._length += 1


    def search(self, value):
        current_node = self._head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False


    def __len__(self):
        return self._length

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.value
            current_node = current_node.next
