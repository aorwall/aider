from collections import deque
import re
class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    class ForthStack(deque):
        def __init__(self):
            super().__init__()

        def push(self, value):
            return self.append(value)

        def pop(self):
            if len(self) < 1:
                raise StackUnderflowError('Attempted to pop from empty stack')
            return super().pop()

        def peek(self):
            if len(self) < 1:
                raise StackUnderflowError('Attempted to peek at empty stack')
            return self[-1]

    def parse_word(match):
        word = match.group(0)

        if word in ('+', '-', '*', '/'):
            return word
        elif word == 'DUP':
            stack.push(stack.peek())
        elif word == 'DROP':
            stack.pop()
        elif word == 'SWAP':
            a = stack.pop()
            b = stack.pop()
            stack.push(a)
            stack.push(b)
        elif word == 'OVER':
            a = stack.pop()
            b = stack.peek()
            stack.push(a)
            stack.push(b)
        else:
            try:
                return int(word)
            except ValueError:
                pass

        raise ValueError("undefined operation")

    program = re.findall(r'\w+|[-+*/()\s]', str(input_data)) # convert input_data into string before passing it to re.findall

    stack = ForthStack()

    for token in program:
        result = parse_word(token)
        if isinstance(result, str):
            if result in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                if   result == '+': stack.push(a + b)
                elif result == '-': stack.push(a - b)
                elif result == '*': stack.push(a * b)
                elif result == '/':
                    if b==0:
                        raise ZeroDivisionError('divide by zero')
                    stack.push(int(a / float(b))) # force division to be integer
            else:
                raise ValueError("undefined operation")
        else:
            stack.push(result)

    return stack.pop()