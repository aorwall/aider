def reverse(text):
    # Initialize empty string to store the reversed text
    rev_str = ""

    # Iterate over the input string backwards and append each character to the output string
    for char in text[::-1]:
        rev_str += char

    # Return the reversed string
    return rev_str
