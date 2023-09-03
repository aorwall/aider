def annotate(minefield):
    def count_adjacent_mines(x, y):
        adjacent = [(i, j) for i in range(max(0, x - 1), min(len(minefield), x + 2)) for j in range(max(0, y - 1), min(len(minefield[0]), y + 2)) if minefield[i][j] == "*"]
        return len(set(adjacent) - {(x,y)})

    result = []
    for i, row in enumerate(minefield):
        new_row = ""
        for j, cell in enumerate(row):
            if cell == "*":
                new_row += "*"
            elif cell == ".":
                num_mines = str(count_adjacent_mines(i, j))
                new_row += num_mines if num_mines else " "
            else:
                raise ValueError("Invalid character in input")
        result.append(new_row)

    return result

# Test cases
print(annotate(['..', '*.']))  # Should print ['  ', '*1']
print(annotate(['.*.', '.**', '...']))  # Should print ['1*1', '***', '   ']
print(annotate(['..*', '*.*', '...']))  # Should print [' *1', '*2 ', '   ']
print(annotate(['....', '*.*.', '*...', '.....']))  # Should print [' 1 ', '*23 ', '   ', '    ']
print(annotate(['.**.', '*.*.', '....', '..*.', '.']))  # Should print ['1*2 ', '*2*2', '   ', '1  ', '   ']
