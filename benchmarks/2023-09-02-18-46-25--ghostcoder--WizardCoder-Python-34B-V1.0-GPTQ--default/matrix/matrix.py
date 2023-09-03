import re
from typing import List
class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [[int(num) for num in row.split()] for row in matrix_string.strip().split('\n')]

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self._matrix]

    @property
    def rows(self):
        return len(self._matrix)

    @property
    def columns(self):
        return len(self._matrix[0]) if self.rows > 0 else 0

    def __str__(self):
        return '\n'.join([' '.join([f"{num}" for num in row]) for row in self._matrix]) + '\n'


def parse_matrix(matrix_string):
    """Parse a string representation of a matrix into a list of lists."""
    return Matrix(matrix_string)

def get_row(matrix_string, index):
    """Get a specific row of the matrix represented by the given string."""
    matrix = parse_matrix(matrix_string)
    return matrix.row(index)

def get_column(matrix_string, index):
    """Get a specific column of the matrix represented by the given string."""
    matrix = parse_matrix(matrix_string)
    return matrix.column(index)
