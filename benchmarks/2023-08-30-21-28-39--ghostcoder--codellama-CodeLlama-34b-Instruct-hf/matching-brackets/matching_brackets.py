def is_paired(input_string):
    opening_brackets = ["[", "{", "("]
    closing_brackets = ["]", "}", ")"]
    stack = []
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack[-1]) != closing_brackets.index(char):
                return False
            stack.pop()
    return not stack
