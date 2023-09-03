class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        self.length = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self.length

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.value)
            current = current.next
        return f"LinkedList({nodes})"

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            raise EmptyListException("The list is empty.")
        value = self.tail.value
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return value

    def reversed(self):
        new_list = LinkedList()
        current = self.tail
        while current:
            new_list.push(current.value)
            current = current.next
        return new_list


class EmptyListException(Exception):
    pass