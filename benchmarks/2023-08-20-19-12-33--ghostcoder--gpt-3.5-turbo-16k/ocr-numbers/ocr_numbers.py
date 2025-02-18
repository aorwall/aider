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

    # Initialize the result string
    result = ""

    # Iterate over the input lines in groups of four
    for i in range(0, len(input_grid), 4):
        # Get the four lines of the current number
        number_lines = input_grid[i:i+4]

        # Check if the number of columns is valid for each line
        if any(len(line) != len(number_lines[0]) for line in number_lines):
            raise ValueError("Number of input columns is not consistent")

        # Iterate over the columns of the current number
        for j in range(0, len(number_lines[0]), 3):
            # Get the three characters of the current column
            column_chars = [line[j:j+3] for line in number_lines]

            # Convert the column characters to a binary font string
            binary_font_str = "".join(column_chars)

            # Check if the binary font string is recognized
            if binary_font_str in binary_font:
                # Append the recognized digit to the result string
                result += binary_font[binary_font_str]
            else:
                # Append a question mark to the result string
                result += "?"

        # Append a comma to the result string if there are more numbers
        if i + 4 < len(input_grid):
            result += ","

    return result