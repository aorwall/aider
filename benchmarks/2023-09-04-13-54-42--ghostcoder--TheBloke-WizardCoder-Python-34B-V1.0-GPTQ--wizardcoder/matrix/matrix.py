class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [[int(num) for num in row.split()] for row in matrix_string.strip().split('\n')]

    def row(self, index):
        if index < 0 or index >= len(self._matrix):
            raise IndexError('Row index out of range')
        return self._matrix[index]

    def column(self, index):
        if index < 0 or index >= len(self._matrix[0]):
            raise IndexError('Column index out of range')
        return [row[index] for row in self._matrix]

def main():
    matrix_string = """1 2 3
        4 5 6
        7 8 9"""
    matrix = Matrix(matrix_string)

    print("Extracted row: ", matrix.row(2)) # Should output [3, 4]
    print("Extracted column: ", matrix.column(3)) # Should output [3, 6, 9]

if __name__ == '__main__':
    main()
