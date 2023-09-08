class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        for value in values:
            self.push(value)

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            raise EmptyListException("The list is empty.")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def reversed(self):
        current_node = self.head
        reversed_list = LinkedList()
        while current_node is not None:
            reversed_list.push(current_node.value)
            current_node = current_node.next
        return reversed_list

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

# Test cases
def test_linked_list():
    ll = LinkedList()
    assert len(ll) == 0

    ll.push(1)
    assert len(ll) == 1
    assert list(iter(ll)) == [1]

    ll.push(2)
    assert len(ll) == 2
    assert list(iter(ll)) == [2, 1]

    assert ll.pop() == 1
    assert len(ll) == 1
    assert list(iter(ll)) == [2]

    assert ll.pop() == 2
    assert len(ll) == 0
    assert list(iter(ll)) == []

    try:
        ll.pop()
    except EmptyListException as e:
        assert str(e) == "The list is empty."
    else:
        assert False, "Expected EmptyListException to be raised"

    ll.push(3)
    assert len(ll) == 1
    assert list(iter(ll)) == [3]

test_linked_list()
