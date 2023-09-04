class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = []
    for token in input_data:
        if token == "+":
            try:
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            except IndexError:
                raise StackUnderflowError("Not enough values on the stack.")
        else:
            try:
                value = int(token)
                stack.append(value)
            except ValueError:
                raise Exception("Invalid syntax")
    return stack
