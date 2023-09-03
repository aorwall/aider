class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    """
    Evaluate the input data and return the result.
    """
    # Initialize the stack
    stack = []

    # Tokenize the input data
    tokens = tokenize(input_data)

    # Iterate over the tokens
    for token in tokens:
        # If the token is a number, push it to the stack
        if is_number(token):
            stack.append(int(token))
        # If the token is a word, evaluate it
        elif is_word(token):
            # Get the definition of the word
            definition = get_definition(token)

            # If the definition is a number, push it to the stack
            if is_number(definition):
                stack.append(int(definition))
            # If the definition is a word, evaluate it
            elif is_word(definition):
                # Recursively evaluate the word
                result = evaluate(definition)

                # If the result is a number, push it to the stack
                if is_number(result):
                    stack.append(result)
                # If the result is a list, extend the stack with it
                elif is_list(result):
                    stack.extend(result)
                else:
                    raise ValueError("Invalid result from word evaluation")
            else:
                raise ValueError("Invalid definition for word")
        # If the token is a list, evaluate each item in the list and extend the stack with the results
        elif is_list(token):
            results = []
            for item in token:
                result = evaluate(item)
                if is_number(result):
                    results.append(result)
                elif is_list(result):
                    results.extend(result)
                else:
                    raise ValueError("Invalid result from list evaluation")
            stack.extend(results)
        else:
            raise ValueError("Invalid token")

    # If the stack is not full, raise an error
    if len(stack) < 1:
        raise StackUnderflowError("Insufficient number of items in stack")

    # Return the top item from the stack
    return stack.pop()


def tokenize(input_data):
    """
    Tokenize the input data and return a list of tokens.
    """
    # Split the input data into tokens
    tokens = input_data.split()

    # Return the list of tokens
    return tokens


def is_number(token):
    """
    Return True if the token is a number, False otherwise.
    """
    try:
        int(token)
        return True
    except ValueError:
        return False


def is_word(token):
    """
    Return True if the token is a word, False otherwise.
    """
    return token.isalpha()


def is_list(token):
    """
    Return True if the token is a list, False otherwise.
    """
    return token.startswith("[") and token.endswith("]")


def get_definition(word):
    """
    Return the definition of the word.
    """
    # Check if the word is a built-in word
    if word in BUILT_IN_WORDS:
        return BUILT_IN_WORDS[word]
    # Check if the word is a user-defined word
    elif word in USER_DEFINED_WORDS:
        return USER_DEFINED_WORDS[word]
    else:
        raise ValueError("Invalid word")


# Dictionary of built-in words
BUILT_IN_WORDS = {
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/",
    "DUP": "DUP",
    "DROP": "DROP",
    "SWAP": "SWAP",
    "OVER": "OVER"
}

# Dictionary of user-defined words
USER_DEFINED_WORDS = {}
