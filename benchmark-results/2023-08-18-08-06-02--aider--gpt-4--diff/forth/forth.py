class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = []
    definitions = {}
    if isinstance(input_data, list):
        input_data = ' '.join(input_data)
    words = input_data.upper().split()

    for word in words:
        if word.isdigit():
            stack.append(int(word))
        elif word in ['+', '-', '*', '/']:
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack for operation")
            b, a = stack.pop(), stack.pop()
            if word == '+':
                stack.append(a + b)
            elif word == '-':
                stack.append(a - b)
            elif word == '*':
                stack.append(a * b)
            elif word == '/':
                if b == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(a // b)
        elif word == 'DUP':
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack for operation")
            stack.append(stack[-1])
        elif word == 'DROP':
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack for operation")
            stack.pop()
        elif word == 'SWAP':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack for operation")
            stack[-2], stack[-1] = stack[-1], stack[-2]
        elif word == 'OVER':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack for operation")
            stack.append(stack[-2])
        elif word == ':':
            name = words.pop(0).upper()
            if name.isdigit():
                raise ValueError("Word definition cannot start with a digit")
            definition = []
            while words[0] != ';':
                definition.append(words.pop(0))
            definitions[name] = definition
        elif word in definitions:
            words = definitions[word] + words
        else:
            raise ValueError("undefined operation")

    return stack
