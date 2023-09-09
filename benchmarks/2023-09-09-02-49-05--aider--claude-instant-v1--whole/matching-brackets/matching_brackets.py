def is_paired(input_string):
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_map = {")":"(", "]":"[", "}":"{"}
    stack = []
    
    for character in input_string:
        if character in opening_brackets:
            stack.append(character)
        elif character in closing_brackets:
            if not stack:
                return False
            current_char = stack.pop()
            if bracket_map[character] != current_char:
                return False
    if stack:
        return False
    return True
