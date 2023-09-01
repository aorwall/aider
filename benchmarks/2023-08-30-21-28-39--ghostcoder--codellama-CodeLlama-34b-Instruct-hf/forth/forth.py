def evaluate(input_data):
    # Parse the input data
    tokens = input_data.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == '+':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            stack.append(stack.pop() - stack.pop())
        elif token == '*':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            try:
                stack.append(stack.pop() / stack.pop())
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero")
        elif token == 'dup':
            if len(stack) < 1:
                raise StackUnderflowError("Stack underflow")
            stack.append(stack[-1])
        elif token == 'drop':
            if len(stack) < 1:
                raise StackUnderflowError("Stack underflow")
            stack.pop()
        elif token == 'swap':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            stack.append(stack.pop())
            stack.append(stack.pop())
        elif token == 'over':
            if len(stack) < 2:
                raise StackUnderflowError("Stack underflow")
            stack.append(stack[-2])
        else:
            raise ValueError("Invalid operation")
    return stack