def is_paired(input_string):
    stack = []
    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']
    bracket_pairs = {'[': ']', '{': '}', '(': ')'}
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != char:
                return False
    
    return len(stack) == 0