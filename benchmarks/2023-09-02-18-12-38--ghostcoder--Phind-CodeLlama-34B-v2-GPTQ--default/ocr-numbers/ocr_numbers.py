def convert(input_grid):
    # Check for correct size
    num_rows = len(input_grid)
    num_cols = len(input_grid[0])

    if (num_rows % 4 != 0) or (num_cols != 3 * (num_rows // 4)):
        raise ValueError("Number of input lines is not a multiple of four")

    # Convert each digit in the grid
    result = []
    for i in range(0, num_rows, 4):
        digit_str = ""
        for j in range(0, num_cols, 3):
            # Classify the digit using its pipes and underscores
            top = input_grid[i][j+1] == " "
            upper_right = input_grid[i][j+2] == "_"
            middle = input_grid[i+1][j+1] == "|"
            lower_left = input_grid[i+2][j+1] == " "
            lower_right = input_grid[i+2][j+2] == " "
            bottom = input_grid[i+3][j+1] == "|"

            # Map this classification to a number
            if top:
                if upper_right:
                    if middle:
                        if lower_left:
                            if bottom:
                                digit_str += "1"
                            else:
                                digit_str += "?"
                        elif lower_right:
                            digit_str += "7"
                        else:
                            digit_str += "8"
                    elif lower_left:
                        digit_str += "2"
                    else:
                        digit_str += "6"
                elif middle:
                    digit_str += "0"
                else:
                    digit_str += "9"
            else:
                if upper_right:
                    digit_str += "5"
                else:
                    digit_str += "4"

        result.append(digit_str)

    return ",".join(result)

