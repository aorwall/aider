class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

def evaluate(input_data):
    stack = []
    
    input_data = " ".join(input_data)
    
    for token in input_data.split():
        if token in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient operands for operator")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(a // b)
        elif token in ["DUP", "DROP", "SWAP", "OVER"]:
            if len(stack) < 1 and token in ["DROP", "SWAP", "OVER"]:
                raise StackUnderflowError("Insufficient items in stack for operation")
            if token == "DUP":
                stack.append(stack[-1])
            elif token == "DROP":
                stack.pop()
            elif token == "SWAP":
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
            elif token == "OVER":
                a = stack.pop()
                b = stack[-1]
                stack.append(a)
                stack.append(b)
                stack.append(a)
        else:
            try:
                val = int(token)
                stack.append(val)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
            
    return stack
