class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


class Forth:
    def __init__(self):
        self.stack = []
        self.words = {}

    def evaluate(self, input_data):
        for word in input_data.split():
            if word.isdigit():
                self.stack.append(int(word))
            elif word.upper() in ['DUP', 'DROP', 'SWAP', 'OVER']:
                self.stack_manipulation(word.upper())
            elif word.upper() in ['+', '-', '*', '/']:
                self.arithmetic_operation(word)
            elif word == ':':
                self.define_new_word(input_data)
                break
            else:
                self.execute_word(word)
        return self.stack

    def stack_manipulation(self, word):
        if word == 'DUP':
            if len(self.stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack.append(self.stack[-1])
        elif word == 'DROP':
            if len(self.stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack.pop()
        elif word == 'SWAP':
            if len(self.stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack[-2], self.stack[-1] = self.stack[-1], self.stack[-2]
        elif word == 'OVER':
            if len(self.stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack.append(self.stack[-2])

    def arithmetic_operation(self, operation):
        if len(self.stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        a, b = self.stack.pop(), self.stack.pop()
        if operation == '+':
            self.stack.append(b + a)
        elif operation == '-':
            self.stack.append(b - a)
        elif operation == '*':
            self.stack.append(b * a)
        elif operation == '/':
            if a == 0:
                raise ZeroDivisionError("divide by zero")
            self.stack.append(b // a)

    def define_new_word(self, input_data):
        words = input_data.split()
        index = words.index(';')
        if index < 3:
            raise ValueError("undefined operation")
        name = words[1]
        definition = ' '.join(words[2:index])
        self.words[name.upper()] = definition

    def execute_word(self, word):
        if word.upper() not in self.words:
            raise ValueError("undefined operation")
        self.evaluate(self.words[word.upper()])


def evaluate(input_data):
    forth = Forth()
    return forth.evaluate(input_data)
