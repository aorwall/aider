from collections import namedtuple
import re

StackEntry = namedtuple('StackEntry', ['operation', 'operands'])

OPERATIONS = {
    'ADD': lambda x, y: x + y,
    'SUBTRACT': lambda x, y: x - y,
    'MULTIPLY': lambda x, y: x * y,
    'DIVIDE': lambda x, y: x // y,
}

COMMANDS = {
    'PUSH': 'push',
    'CALL': 'call',
}

class StackUnderflowError(Exception):
    pass


def evaluate(program):
    stack = []

    for line in program:
        match = re.match(r'^(\w+) (?:\d+ )?(?:(?:(\d+)\s)?(.*))?$', line)
        command, arg1, arg2 = match.groups()

        if command == 'PUSH':
            try:
                operand = int(arg1)
            except TypeError:
                raise ValueError(f"Invalid literal on line '{line}'")

            stack.append(StackEntry(None, operand))
        elif command == 'CALL':
            operation = OPERATIONS.get(arg1)
            if operation is None:
                raise ValueError(f"Unknown operation '{arg1}' on line '{line}'")

            if len(stack) < 2:
                raise StackUnderflowError(f"Not enough values on the stack to execute '{arg1}' on line '{line}'")

            b, a = stack[-1], stack[-2]
            result = operation(a, b)
            del stack[-2:]
            stack.append(StackEntry(arg1, result))

    return [entry.operands for entry in stack]


def evaluate(input_data):
    pass
