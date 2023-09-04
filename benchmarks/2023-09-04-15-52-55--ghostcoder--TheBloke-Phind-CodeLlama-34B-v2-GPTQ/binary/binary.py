def parse_binary(binary_string):
    try:
        # Check if each character in the string is either '0' or '1'. If not, raise a ValueError.
        for char in binary_string:
            if char != '0' and char != '1':
                raise ValueError()

        # Calculate the decimal equivalent of the binary string.
        decimal = 0
        for index, bit in enumerate(reversed(binary_string)):
            decimal += int(bit) * pow(2, index)

        return decimal

    except ValueError:
        print('Invalid binary literal: {}'.format(binary_string))
        return None
