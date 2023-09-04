def parse_binary(binary_string):
    try:
        # Check if all characters in the string are either 0 or 1
        if not all(char in ('0', '1') for char in binary_string):
            raise ValueError("Invalid binary literal: " + binary_string)

        # Convert the binary string to decimal
        decimal = int(binary_string, 2)

        return decimal

    except ValueError as e:
        raise ValueError("Invalid binary literal: " + binary_string) from None
