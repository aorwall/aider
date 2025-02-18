import operator
import re
from collections import deque

OPERATIONS = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiplied by': operator.mul,
    'divided by': operator.truediv
}

def apply_operation(stack, op):
    b = stack.pop()
    a = stack.pop()
    return a + op(b, a)

def parse_question(question):
    nums = list(map(int, re.findall('\d+', question)))
    words = re.split('\d+', question)[:-1]

    if len(nums) != len(words) - 1:
        raise ValueError('syntax error')

    for word in words:
        if word not in OPERATIONS:
            raise ValueError('unknown operation')

    return nums, words

def answer(question):
    try:
        nums, words = parse_question(question)

        stack = deque([nums[0]])
        for i in range(len(words)):
            if words[i] in OPERATIONS:
                stack.appendleft(apply_operation(deque(stack[-2:]), OPERATIONS[words[i]]))
                nums = nums[1:]
            else:
                raise ValueError('syntax error')

        while len(stack) > 1:
            stack = deque([apply_operation(deque(stack[-2:]), OPERATIONS[words[i]])])

        return int(stack[0])
    except ValueError as e:
        print(f"Invalid question '{question}' because {str(e)}")
        return None
