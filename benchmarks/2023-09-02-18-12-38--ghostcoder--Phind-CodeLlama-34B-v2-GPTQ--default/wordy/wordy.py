import re
def answer(question):
    operations = {
        'plus': lambda x, y: x + y,
        'minus': lambda x, y: x - y,
        'multiplied by': lambda x, y: x * y,
        'divided by': lambda x, y: x / y if y != 0 else 'undefined',
    }

    # Remove unnecessary spaces and convert to lowercase
    question = question.replace('?', '').strip().lower()

    for op in operations:
        if op in question:
            parts = question.split(' ')
            index_op = parts.index(op)

            if len(parts[index_op-2:index_op]) == 3:
                num1, op, num2 = parts[index_op-2:index_op]
            elif len(parts[index_op-1:index_op+1]) == 3:
                num1, op, num2 = parts[index_op-1:index_op+1]

            try:
                result = operations[op](int(num1), int(num2))

                if isinstance(result, int):
                    return result
                elif isinstance(result, float):
                    return round(result)
            except ZeroDivisionError:
                raise ValueError("Can't divide by zero")
            except Exception as e:
                raise ValueError(str(e))

    raise ValueError("Invalid syntax")
