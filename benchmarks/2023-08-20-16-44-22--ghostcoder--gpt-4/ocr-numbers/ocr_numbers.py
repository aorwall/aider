def convert(input_grid):
    # Define the 3x4 grid representation of each digit
    digits = {
        " _ \n| |\n|_|\n   ": "0",
        "   \n  |\n  |\n   ": "1",
        " _ \n _|\n|_ \n   ": "2",
        " _ \n _|\n _|\n   ": "3",
        "   \n|_|\n  |\n   ": "4",
        " _ \n|_ \n _|\n   ": "5",
        " _ \n|_ \n|_|\n   ": "6",
        " _ \n  |\n  |\n   ": "7",
        " _ \n|_|\n|_|\n   ": "8",
        " _ \n|_|\n _|\n   ": "9",
    }

    # Check if the input grid is a valid size
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    # Split the input grid into lines
    lines = [input_grid[i:i+4] for i in range(0, len(input_grid), 4)]

    # Convert each line to a number
    numbers = []
    for line in lines:
        number = ""
        for i in range(0, len(line[0]), 3):
            chunk = "\n".join(row[i:i+3] for row in line)
            number += digits.get(chunk, "?")
        numbers.append(number)

    return ",".join(numbers)