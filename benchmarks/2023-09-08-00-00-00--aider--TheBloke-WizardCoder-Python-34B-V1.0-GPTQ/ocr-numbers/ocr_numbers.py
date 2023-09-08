def convert(input_grid):
    """
    Given a 3 x 4 grid of pipes, underscores, and spaces, determine which number is represented,
    or whether it is garbled.

    Args:
        input_grid (str): A string representing the input grid.

    Returns:
        str: A string representing the converted number, or '?' if it is garbled, or an error message if the input is incorrect.
    """

    def recognize_number(binary_string):
        if len(binary_string) != 4:
            raise ValueError("Number of input lines is not a multiple of four")
        if len(binary_string[0]) != 3:
            raise ValueError("Number of input columns is not a multiple of three")

        number = ""
        for row in binary_string:
            if row == " _ ":
                number += "0"
            elif row == "| |":
                number += "1"
            else:
                number += "?"

        return number

    binary_strings = []
    for i in range(0, len(input_grid), 4):
        binary_strings.append(input_grid[i:i+4])

    numbers = []
    for binary_string in binary_strings:
        try:
            numbers.append(recognize_number(binary_string))
        except ValueError as e:
            return str(e)

    return ",".join(numbers)
