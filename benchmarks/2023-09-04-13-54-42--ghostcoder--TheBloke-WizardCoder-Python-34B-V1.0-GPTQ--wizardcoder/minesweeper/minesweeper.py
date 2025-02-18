def annotate(minefield):
    rows = len(minefield)
    cols = len(minefield[0])

    def count_adjacent_mines(row, col):
        count = 0

        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == 0 and c == 0:
                    continue

                new_row = row + r
                new_col = col + c

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if minefield[new_row][new_col] == "*":
                        count += 1

        return count

    annotated_minefield = []

    for row in range(rows):
        annotated_row = ""
        for col in range(cols):
            if minefield[row][col] != " ":
                annotated_row += str(count_adjacent_mines(row, col))
            else:
                annotated_row += " "
        annotated_minefield.append(annotated_row)

    return annotated_minefield

# Test cases
assert annotate([[" ", "*", " ", " "], ["*", "*", "*", " "], [" ", "*", " ", " "]]) \
       == [['1', '*', '1', ' '], [' ', '*', ' ', ' '], [' ', '*', ' ', ' ']]

assert annotate([[" ", "*", " ", " ", " "], [" ", "*", "*", "*", " "], [" ", " ", " ", "*", " "], ["*", "*", "*", "*", "*"]]) \
       == [['1', '2', '1', ' ', ' '], [' ', '*', '*', '*', ' '], [' ', ' ', ' ', '*', ' '], ['*', '*', '*', '*', '*']]

try:
    annotate([[" ", "a", " ", " "], ["*", "*", "*", " "], [" ", "*", " ", " "]])
except ValueError as e:
    assert str(e) == "Invalid input: board contains non-space and non-asterisk characters."
