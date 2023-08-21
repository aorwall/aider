def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    numbers = {
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

    result = ""
    for i in range(0, len(input_grid), 4):
        for j in range(0, len(input_grid[i]), 3):
            segment = "\n".join(row[j:j+3] for row in input_grid[i:i+4])
            result += numbers.get(segment, "?")
        result += ","
    return result.rstrip(",")
