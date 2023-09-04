import re
from typing import List

OPERATIONS = {
    'plus': lambda x, y: x + y,
    'minus': lambda x, y: x - y,
    'multiplied by': lambda x, y: x * y,
    'divided by': lambda x, y: x // y, # Change here from `/` to `//` for integer division
}

def extract_numbers(text: str) -> List[int]:
    return list(map(int, re.findall(r'-?\d+', text)))

def extract_operations(text: str) -> List[str]:
    pattern = r"\b(?:" + '|'.join(OPERATIONS.keys()) + r")\b"
    return re.findall(pattern, text, flags=re.IGNORECASE)

def validate_question(question: str) -> bool:
    if len(extract_numbers(question)) != len(extract_operations(question)) + 1:
        return False

    for op in extract_operations(question):
        if op not in OPERATIONS:
            return False

    try:
        eval(question.strip(' ?').replace('x', '*'))
    except SyntaxError:
        return False

    return True

def calculate(expression: str) -> int:
    nums = extract_numbers(expression)
    ops = extract_operations(expression)

    total = nums[0]
    for i, op in enumerate(ops):
        total = OPERATIONS[op.lower()](total, nums[i + 1])

    return total

def answer(question: str) -> int:
    if not validate_question(question):
        raise ValueError("syntax error")

    return calculate(question)