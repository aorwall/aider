import re
from collections import deque
from collections import defaultdict

def is_paired(input_string):
    stack = deque()
    mapping = {"(": ")", "[": "]", "{": "}"}

    for char in input_string:
        if char in mapping:
            stack.append(char)
        elif len(stack) > 0 and char == mapping[stack[-1]]:
            stack.pop()

    return len(stack) == 0
