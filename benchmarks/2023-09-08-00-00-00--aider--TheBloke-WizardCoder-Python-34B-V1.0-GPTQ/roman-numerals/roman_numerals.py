def roman(number):
    """
    Convert a normal number to a Roman numeral.

    :param number: A positive integer between 1 and 3999.
    :return: The Roman numeral representation of the number.
    """
    if not isinstance(number, int) or number < 1 or number > 3999:
        raise ValueError("Number must be an integer between 1 and 3999")

    roman_numeral_mapping = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for value, numeral in roman_numeral_mapping.items():
        while number >= value:
            result += numeral
            number -= value

    return result
