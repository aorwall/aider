class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


class Stack:
    def __init__(self):
        self._stack = []


    def push(self, value):
        self._stack.append(value)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            raise StackUnderflowError('Stack Underflow Error')

    def peek(self):
        try:
            return self._stack[-1]
        except IndexError:
            raise StackUnderflowError('Stack Underflow Error')

    @property
    def size(self):
        return len(self._stack)

    def clear(self):
        self._stack.clear()


def evaluate(input_data):
    stack = Stack()
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '%': lambda x, y: x % y,
        '<': lambda x, y: int(x < y),
        '>': lambda x, y: int(x > y),
        '==': lambda x, y: int(x == y),
        '>=': lambda x, y: int(x >= y),
        '<=': lambda x, y: int(x <= y),
        '!=': lambda x, y: int(x != y),
        'dup': lambda x: stack.push(x)
    }
    tokens = input_data.split()
    for token in tokens:
        try:
            if token.isdigit():
                stack.push(int(token))
            elif token in ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = ops[token](arg1, arg2)
                stack.push(result)
            else:
                raise ValueError(f'"{token}" is not a valid operator or operand')
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot divide by zero')
        except TypeError:
            raise TypeError('Invalid data type provided')
    return stack.peek()
