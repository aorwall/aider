def annotate(minefield):
    # Function body starts here
    def count_adjacent_mines(x, y):
        adjacent = [(i, j) for i in range(max(0, x - 1), min(len(minefield), x + 2)) for j in range(max(0, y - 1), min(len(minefield[0]), y + 2)) if (i, j) != (x, y)]
        return sum([1 for i, j in adjacent if minefield[i][j] == '*'])

    for row in range(len(minefield)):
        for col in range(len(minefield[row])):
            if minefield[row][col] == ' ':
                minefield[row][col] = str(count_adjacent_mines(row, col))

    return minefield


def board():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows < 1 or cols < 1:
            raise ValueError("Invalid input: Rows and Columns must be greater than zero.")

        minefield = [[' ' * cols for _ in range(rows)]
        num_mines = int(input("Enter number of mines: "))
        
        if num_mines > rows * cols:
            raise ValueError("Too many mines for the given size of the board.")

        while num_mines > 0:
            r, c = random.randint(0, rows - 1), random.randint(0, cols - 1)
            if minefield[r][c] != '*':
                minefield[r][c] = '*'
                num_mines -= 1

        annotate(minefield)
        print('\n'.join([''.join(row) for row in minefield]))

    except ValueError as e:
        print(e)
