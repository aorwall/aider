class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""
    def __init__(self, message):
        self.message = message
        
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.items:
            raise StackUnderflowError("Insufficient items in stack")
        return self.items.pop()
        
def evaluate(input_data):
    stack = Stack()
    words = {
        "+": lambda a,b: b + a,
        "-": lambda a,b: b - a,
        "*": lambda a,b: b * a, 
        "/": lambda a,b: b // a,
        "DUP": lambda a: (a,a),
        "DROP": lambda a: (),
        "SWAP": lambda a,b: (b,a),
        "OVER": lambda a,b: (b,a,b)
    }
    
    for token in input_data:
        if token.isdigit():
            stack.push(int(token))
        elif token in words:
            try:
                func = words[token]
                args = [stack.pop() for _ in range(func.__code__.co_argcount)]
                result = func(*args)
                for r in result:
                    stack.push(r)
            except IndexError:
                raise StackUnderflowError("Insufficient items in stack")
        else:
            try:
                func = words[token.lower()]
                args = [stack.pop() for _ in func.__code__.co_argcount]
                result = func(*args)
                for r in result:
                    stack.push(r)
            except KeyError:
                raise ValueError("Undefined operation")
            
    return stack.items
