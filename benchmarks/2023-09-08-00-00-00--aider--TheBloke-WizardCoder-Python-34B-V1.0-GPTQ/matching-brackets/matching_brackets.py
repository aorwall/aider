def is_paired(input_string):
    stack = []
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        if char in brackets_dict.values():
            stack.append(char)
        elif char in brackets_dict.keys():
            if not stack or brackets_dict[char] != stack.pop():
                return False
    
    return len(stack) == 0
