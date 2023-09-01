import re
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def answer(question):
    # Use regular expressions to extract the numbers and operations
    numbers = re.findall(r'\d+', question)
    operations = re.findall(r'[+-*/]', question)

    # Evaluate the expression
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operations[i - 1] == '+':
            result += numbers[i]
        elif operations[i - 1] == '-':
            result -= numbers[i]
        elif operations[i - 1] == '*':
            result *= numbers[i]
        elif operations[i - 1] == '/':
            result /= numbers[i]
    return result
