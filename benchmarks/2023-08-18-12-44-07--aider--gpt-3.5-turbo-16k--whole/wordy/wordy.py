def answer(question):
    # Split the question into individual words
    words = question.split()

    # Check if the question is asking for a number
    if len(words) == 3 and words[0] == "What" and words[1] == "is":
        try:
            # Try to convert the last word into an integer
            number = int(words[2])
            return number
        except ValueError:
            raise ValueError("Invalid number")

    # Check if the question is asking for an addition
    if len(words) == 5 and words[0] == "What" and words[1] == "is" and words[3] == "plus":
        try:
            # Try to convert the first and last words into integers
            number1 = int(words[2])
            number2 = int(words[4].rstrip('?'))
            return number1 + number2
        except ValueError:
            raise ValueError("Invalid addition")

    # Check if the question is asking for a subtraction
    if len(words) == 5 and words[0] == "What" and words[1] == "is" and words[3] == "minus":
        try:
            # Try to convert the first and last words into integers
            number1 = int(words[2])
            number2 = int(words[4].rstrip('?'))
            return number1 - number2
        except ValueError:
            raise ValueError("Invalid subtraction")

    # Check if the question is asking for a multiplication
    if len(words) == 7 and words[0] == "What" and words[1] == "is" and words[3] == "multiplied" and words[4] == "by":
        try:
            # Try to convert the first and last words into integers
            number1 = int(words[2])
            number2 = int(words[6].rstrip('?'))
            return number1 * number2
        except ValueError:
            raise ValueError("Invalid multiplication")

    # Check if the question is asking for a division
    if len(words) == 7 and words[0] == "What" and words[1] == "is" and words[3] == "divided" and words[4] == "by":
        try:
            # Try to convert the first and last words into integers
            number1 = int(words[2])
            number2 = int(words[6].rstrip('?'))
            return number1 / number2
        except ValueError:
            raise ValueError("Invalid division")

    # Check if the question is asking for multiple operations
    if len(words) >= 7 and words[0] == "What" and words[1] == "is":
        try:
            # Initialize the result with the first number
            result = int(words[2])

            # Iterate over the remaining words in pairs
            for i in range(3, len(words), 2):
                # Check if the pair represents an operation
                if words[i] == "plus":
                    result += int(words[i+1].rstrip('?'))
                elif words[i] == "minus":
                    result -= int(words[i+1].rstrip('?'))
                elif words[i] == "multiplied" and words[i+1] == "by":
                    result *= int(words[i+2].rstrip('?'))
                elif words[i] == "divided" and words[i+1] == "by":
                    result /= int(words[i+2].rstrip('?'))
                else:
                    raise ValueError("Unknown operation")

            return result
        except ValueError:
            raise ValueError("Invalid operation")

    # If none of the above conditions are met, raise an error
    raise ValueError("Invalid question")
