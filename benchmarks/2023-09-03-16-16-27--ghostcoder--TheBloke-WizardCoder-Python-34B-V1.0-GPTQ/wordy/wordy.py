import re
from collections import deque


class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values


def tokenize(question):
    tokens = re.findall(r'\b\w+\b', question)
    return tokens


def parse(tokens):
    linked_list = LinkedList()
    for token in tokens:
        if token.isdigit():
            linked_list.add_node(int(token))
        elif token in ('plus', 'minus', 'multiplied', 'divided'):
            linked_list.add_node(token)
        else:
            raise ValueError("Syntax error: Invalid character found.")
    return linked_list


def calculate(linked_list):
    stack = deque()
    operators = {
        'plus': lambda x, y: x + y,
        'minus': lambda x, y: x - y,
        'multiplied': lambda x, y: x * y,
        'divided': lambda x, y: x / y
    }

    curr = linked_list.head
    while curr:
        if isinstance(curr.value, int):
            stack.append(curr.value)
        elif curr.value in operators:
            if len(stack) >= 2:
                right_operand = stack.pop()
                left_operand = stack.pop()
                operation = operators[curr.value]
                result = operation(left_operand, right_operand)
                stack.append(result)
            else:
                raise ValueError("Invalid syntax: Missing operand before operator.")
        else:
            raise ValueError("Unknown operation.")

        curr = curr.next

    if len(stack) > 1:
        raise ValueError("Invalid syntax: Extraneous operands or operators at the end.")

    return stack[-1]


def answer(question):
    try:
        tokens = tokenize(question)
        parsed_list = parse(tokens)
        return calculate(parsed_list)
    except ValueError as e:
        print(str(e))
        return None
