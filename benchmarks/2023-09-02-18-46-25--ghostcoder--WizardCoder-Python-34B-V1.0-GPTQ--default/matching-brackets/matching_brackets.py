def is_paired(input_string):
    """
    Given a string containing brackets, determine whether each pair is properly nested.
    
    Args:
        input_string (str): A string containing brackets [](){}
    Returns:
        bool: True if all brackets are paired and nested correctly, False otherwise.
    """
    # Create an empty stack to store opening brackets
    stack = []
    # Dictionary to map closing brackets with their respective opening ones
    mappings = {')': '(', ']': '[', '}': '{'}
    # Loop through each character in the input string
    for char in input_string:
        # If it's an opening bracket, add it to the stack
        if char in ['{', '[', '(']:
            stack.append(char)
        # If it's a closing bracket, check if it matches the last opening bracket added to the stack
        elif char in [']', ')', '}']:
            if len(stack) == 0 or mappings[char] != stack[-1]:
                return False
            else:
                stack.pop()
    # If there are no more characters left in the string and all pairs have been matched, return True
    return len(stack) == 0
