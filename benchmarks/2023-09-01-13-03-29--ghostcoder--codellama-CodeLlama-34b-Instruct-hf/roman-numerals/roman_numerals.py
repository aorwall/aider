def roman(number):
    """
    Convert an integer to a Roman numeral.
    
    Args:
        number (int): The number to convert.
    
    Returns:
        str: The Roman numeral representation of the number.
    """
    roman_numerals = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    result = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            result += numeral
            number -= value

    return result

