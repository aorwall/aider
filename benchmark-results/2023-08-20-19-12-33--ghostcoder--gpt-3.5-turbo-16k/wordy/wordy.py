def answer(question):
    # Remove the pass statement
    # Split the question into a list of words
    words = question.split()

    # Check if the question starts with "What is"
    if words[0] != "What" or words[1] != "is":
        raise ValueError("syntax error")

    # Remove the first three words ("What is")
    words = words[2:]

    # Initialize the result variable
    result = None

    # Initialize the operation variable
    operation = None

    # Iterate over the words in the question
    i = 0
    while i < len(words):
        # Check if the word is a number
        if words[i].isdigit():
            # Convert the word to an integer
            number = int(words[i])

            # If this is the first number, assign it to the result variable
            if result is None:
                result = number
            else:
                # If there is a previous operation, perform it with the current number
                if operation == "plus":
                    result += number
                elif operation == "minus":
                    result -= number
                elif operation == "multiplied":
                    result *= number
                elif operation == "divided":
                    result /= number
                else:
                    raise ValueError("unknown operation")

        # Check if the word is an operation
        elif words[i] in ["plus", "minus", "multiplied", "divided"]:
            operation = words[i]

        # If the word is not a number or an operation, raise an error
        else:
            raise ValueError("syntax error")

        # Move to the next word
        i += 1

    # Return the result
    return result