# subclassing the Exception to create a StackUnderflowError
class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

def evaluate(input_str):
    stack = []
    words = input_str.split()

    for word in words:
        try:
            stack.append(int(word))
        except ValueError:
            if word in operations:
                operations[word](stack)
            else:
                raise ValueError("undefined operation")

    return stack