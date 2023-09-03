def is_paired(input_string):
    # Define a dictionary mapping closing brackets to their corresponding opening brackets
    opening_to_closing = {'}': '{', ']': '[', ')': '('}

    # Initialize an empty stack
    stack = []

    for char in input_string:
        if char in opening_to_closing.values():  # If the current character is an opening bracket
            stack.append(char)
        elif char in opening_to_closing:  # If the current character is a closing bracket
            if not stack or opening_to_closing[char] != stack[-1]:  # The brackets are not matched
                return False
            else:  # The brackets are matched
                stack.pop()

    # At the end, the stack should be empty if all pairs were correctly closed and nested
    return len(stack) == 0
