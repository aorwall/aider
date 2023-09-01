def say(number):
    """
    Converts a number to its English pronunciation.
    
    Args:
        number: The number to convert.
    
    Returns:
        The English pronunciation of the number.
    
    Raises:
        ValueError: If the number is out of range.
    """
    if not (0 <= number <= 999999999999):
        raise ValueError("Number out of range")

    # Convert the number to a list of its digits
    digits = [int(digit) for digit in str(number)]

    # Create a list to store the words for each digit
    words = []

    # Iterate over the digits and add the corresponding word to the list
    for i, digit in enumerate(digits):
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
        elif digit == 9:
            words.append("nine")

    # Join the words with a space between each one
    return " ".join(words)
