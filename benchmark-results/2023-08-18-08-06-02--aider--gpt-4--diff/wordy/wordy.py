def answer(question):
    # Check if the question is valid
    if not question.startswith('What is ') or not question.endswith('?'):
        raise ValueError("syntax error")

    # Remove 'What is ' and '?'
    question = question[8:-1]

    # Split the question into parts
    parts = [part for part in re.split(r'(\D+)', question) if part.strip()]

    # Initialize the answer with the first number
    answer = int(parts[0])

    # Iterate over the rest of the parts
    for i in range(1, len(parts), 2):
        # Get the operation and the next number
        operation = parts[i].strip()
        number = int(parts[i+1].strip())

        # Perform the operation
        if operation == 'plus':
            answer += number
        elif operation == 'minus':
            answer -= number
        elif operation == 'multiplied':
            answer *= number
        elif operation == 'divided':
            answer //= number
        else:
            raise ValueError("unknown operation")

    return answer
import re
