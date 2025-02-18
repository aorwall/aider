class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = []
    words = input_data.split()
    for word in words:
        if word.isdigit():
            stack.append(int(word))
        elif word == '+':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
        elif word == '-':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
        elif word == '*':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
        elif word == '/':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                a = stack.pop()
                b = stack.pop()
                if a == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(b // a)
        elif word == 'DUP':
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                stack.append(stack[-1])
        elif word == 'DROP':
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                stack.pop()
        elif word == 'SWAP':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
        elif word == 'OVER':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                a = stack[-2]
                stack.append(a)
        else:
            raise ValueError("undefined operation")
    return stack[-1]