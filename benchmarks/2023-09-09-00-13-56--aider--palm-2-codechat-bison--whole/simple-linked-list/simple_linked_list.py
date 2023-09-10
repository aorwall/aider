class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        for value in values:
            self.push(value)

    def __len__(self):
        """Return the number of elements in the linked list."""
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def head(self):
        """Return the first element in the linked list."""
        if self.head is None:
            raise EmptyListException("The list is empty.")
        return self.head.value

    def push(self, value):
        """Add a new element to the front of the linked list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Remove and return the first element in the linked list."""
        if self.head is None:
            raise EmptyListException("The list is empty.")
        value = self.head.value
        self.head = self.head.next
        return value

    def reversed(self):
        """Return a new linked list with the elements in reverse order."""
        reversed_list = LinkedList()
        node = self.head
        while node is not None:
            reversed_list.push(node.value)
            node = node.next
        return reversed_list


class EmptyListException(Exception):
    """Exception raised when the linked list is empty."""

