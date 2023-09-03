def is_paired(input_string):
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{"}

    for char in input_string:
        if char in brackets_map:
            if not stack or stack[-1] != brackets_map[char]:
                return False
            else:
                stack.pop()
        elif char in brackets_map.values():
            stack.append(char)

    return len(stack) == 0
