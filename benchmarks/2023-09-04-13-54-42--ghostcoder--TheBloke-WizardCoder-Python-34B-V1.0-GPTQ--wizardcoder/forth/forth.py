import re
from collections import deque

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    dictionary = {}

    # Helper functions
    stack = deque()

    def push(value):
        stack.appendleft(value)

    def pop():
        try:
            return stack.popleft()
        except IndexError:
            raise StackUnderflowError("Insufficient number of items in stack")

    def perform(word):
        if word == '+':
            push(pop() + pop())
        elif word == '-':
            value1 = pop()
            value2 = pop()
            push(value2 - value1)
        elif word == '*':
            push(pop() * pop())
        elif word == '/':
            value1 = pop()
            value2 = pop()
            if value1 == 0:
                raise ZeroDivisionError("divide by zero")
            else:
                push(value2 // value1)
        elif word == 'dup':
            push(stack[-1])
        elif word == 'drop':
            pop()
        elif word == 'swap':
            value1 = pop()
            value2 = pop()
            push(value1)
            push(value2)
        elif word == 'over':
            push(stack[-1])
        else:
            raise ValueError("undefined operation")

    # Main loop
    lines = input_data.split('\n')
    for line in lines:
        tokens = re.findall(r'\w+|\d+', line)
        for token in tokens:
            if token.isdigit():
                push(int(token))
            elif token in dictionary:
                dictionary[token].evaluate(push, pop)
            else:
                perform(token.lower())

    return list(stack)
