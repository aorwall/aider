def say(number):
    """
    Return the English words for the given number.
    
    Args:
        number: An integer from 0 to 999,999,999,999 inclusive.
    
    Returns:
        The English words for the given number.
    
    Raises:
        ValueError: If the input is not within the accepted range.
    """
    # Check if the input is valid
    if not (0 <= number <= 999999999999):
        raise ValueError("Input out of range")

    # Convert the number to a string
    number_str = str(number)

    # Get the individual digits of the number
    digits = []
    for char in number_str:
        digits.append(int(char))

    # Initialize the empty list to store the words
    words = []

    # Get the number of digits in the number
    num_digits = len(digits)

    # Loop through each digit and add its corresponding word to the list
    for i in range(num_digits):
        # Get the current digit
        digit = digits[i]

        # Add the corresponding word to the list
        if digit == 0:
            words.append("zero")
        elif digit == 1:
            words.append("one")
        elif digit == 2:
            words.append("two")
        elif digit == 3:
            words.append("three")
        elif digit == 4:
            words.append("four")
        elif digit == 5:
            words.append("five")
        elif digit == 6:
            words.append("six")
        elif digit == 7:
            words.append("seven")
        elif digit == 8:
            words.append("eight")
        else:
            words.append("nine")

    # Join the words in the list to form a single string
    result = " ".join(words)

    return result
