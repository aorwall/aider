class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        node = Node(value, self.head)
        self.head = node
        return node

    def pop(self):
        if self.head == None:
            raise IndexError("Cannot pop from an empty list")
        else:
            popped_node = self.head
            self.head = self.head.succeeding
            return popped_node

    def shift(self):
        if self.head == None:
            raise IndexError("Cannot shift from an empty list")
        else:
            shifted_node = self.head
            self.head = self.head.succeeding
            return shifted_node

    def unshift(self, value):
        node = Node(value, self.head)
        self.head = node
        return node

    def count(self):
        counter = 0
        curr_node = self.head
        while curr_node != None:
            counter += 1
            curr_node = curr_node.succeeding
        return counter

    def delete(self, value):
        curr_node = self.head
        prev_node = None
        found = False
        while curr_node != None and not found:
            if curr_node.value == value:
                found = True
            else:
                prev_node = curr_node
                curr_node = curr_node.succeeding
        if found:
            if prev_node == None:
                self.head = curr_node.succeeding
            else:
                prev_node.succeeding = curr_node.succeeding
            return True
        else:
            return False

    def reverse(self):
        curr_node = self.head
        next_node = None
        prev_node = None
        while curr_node != None:
            next_node = curr_node.succeeding
            curr_node.succeeding = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def display(self):
        values = []
        curr_node = self.head
        while curr_node != None:
            values.append(curr_node.value)
            curr_node = curr_node.succeeding
        print(values)
