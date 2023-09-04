def roman(number):
    """Convert an integer to Roman numeral"""
    # Create a dictionary to map numbers to Roman numerals
    num_dict = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    # Initialize an empty string to store the Roman numeral
    roman_numeral = ''

    # Loop through the digits of the number
    while number > 0:
        # If the digit is 4, we need to represent it as V-I (5-1)
        if number % 10 == 4:
            roman_numeral += num_dict[5] + num_dict[1]
        # If the digit is 9, we need to represent it as X-I (10-1)
        elif number % 10 == 9:
            roman_numeral += num_dict[10] + num_dict[1]
        else:
            # Get the corresponding Roman numeral for the digit
            roman_numeral += num_dict[number % 10]

        # Move to the next digit
        number //= 10

    return roman_numeral

