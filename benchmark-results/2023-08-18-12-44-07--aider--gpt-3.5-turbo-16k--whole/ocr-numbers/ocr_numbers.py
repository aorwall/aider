def convert(input_grid):
    # Check if the number of input lines is a multiple of four
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Check if the number of input columns is a multiple of three
    if any(len(line) % 3 != 0 for line in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    # Define the binary font dictionary
    binary_font = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9"
    }

    # Convert the input grid to binary strings
    binary_strings = []
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[i]), 3):
            binary_string = ""
            for k in range(4):
                binary_string += input_grid[i+k][j:j+3]
            binary_strings.append(binary_string)

    # Convert the binary strings to numbers
    numbers = []
    for binary_string in binary_strings:
        if binary_string in binary_font:
            numbers.append(binary_font[binary_string])
        else:
            numbers.append("?")

    # Join the numbers with commas
    return "".join(numbers)
