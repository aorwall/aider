class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = []
    words = {}

    def apply_op(op):
        if op in ['+', '-', '*', '/']:
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            b, a = stack.pop(), stack.pop()
            if op == '+':
                stack.append(a + b)
            elif op == '-':
                stack.append(a - b)
            elif op == '*':
                stack.append(a * b)
            elif op == '/':
                if b == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(a // b)
        elif op == 'dup':
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-1])
        elif op == 'drop':
            if len(stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.pop()
        elif op == 'swap':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack[-2], stack[-1] = stack[-1], stack[-2]
        elif op == 'over':
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-2])

    for line in input_data:
        tokens = line.lower().split()
        if tokens[0] == ':':
            words[tokens[1]] = tokens[2:-1]
        else:
            for token in tokens:
                if token.isdigit():
                    stack.append(int(token))
                elif token in words:
                    for word in words[token]:
                        if word.isdigit():
                            stack.append(int(word))
                        else:
                            apply_op(word)
                elif token in ['+', '-', '*', '/', 'dup', 'drop', 'swap', 'over']:
                    apply_op(token)
                else:
                    raise ValueError("undefined operation")

    return stack