class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()] for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]

# Example usage:
matrix_string = "9 8 7\n5 3 2\n6 6 7"
matrix = Matrix(matrix_string)

# Get the first row
print(matrix.row(1))  # Output: [9, 8, 7]

# Get the second column
print(matrix.column(2))  # Output: [8, 3, 6]
