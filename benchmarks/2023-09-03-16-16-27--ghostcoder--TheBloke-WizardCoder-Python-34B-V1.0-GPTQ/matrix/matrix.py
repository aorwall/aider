class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [[int(num) for num in line.split()] for line in matrix_string.strip().split('\n')]


    def row(self, index):
        return self._matrix[index - 1] if 0 < index <= len(self._matrix) else []


    def column(self, index):
        return [row[index - 1] for row in self._matrix] if 0 < index <= len(self._matrix[0]) else []
