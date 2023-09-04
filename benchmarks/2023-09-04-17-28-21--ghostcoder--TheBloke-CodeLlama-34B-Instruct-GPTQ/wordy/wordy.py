from typing import List
import re

OPERATIONS = {
    'plus': lambda x, y: x + y,
    'minus': lambda x, y: x - y,
    'multiplied by': lambda x, y: x * y,
    'divided by': lambda x, y: x / y
}

def answer(question: str) -> int:
    """
    Takes a arithmetic word problem and returns its solution.
    """
    # Tokenize the question
    tokens: List[str] = re.split('(\W+)', question)

    # Parse the question
    numbers: List[int] = []
    operators: List[str] = []
    for token in tokens:
        if token.isdigit():
            numbers.append(int(token))
        elif token in OPERATIONS:
            operators.append(token)
        else:
            continue

    # Evaluate the expression
    result = numbers[0]
    for operator, num in zip(operators, numbers[1:]):
        result = OPERATIONS[operator](result, num)

    return result