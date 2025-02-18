import re

def is_paired(input_string):
    # Remove non-bracket characters from input string
    clean_string = re.sub('[^(){}[]]+', '', input_string)

    # Initialize a stack to hold opening brackets
    stack = []

    # Iterate through clean_string
    for char in clean_string:
        if char in ['(', '{', '[']:
            # Push opening brackets onto the stack
            stack.append(char)
        elif char in [')', '}', ']']:
            # Pop closing brackets off the stack
            if len(stack) > 0:
                top = stack.pop()

                # Check if the popped character matches the current character
                if (top == '(' and char != ')') or \
                   (top == '{' and char != '}') or \
                   (top == '[' and char != ']'):
                    return False

    # If the stack is empty after iterating through the entire string, then all brackets are paired properly
    return len(stack) == 0
