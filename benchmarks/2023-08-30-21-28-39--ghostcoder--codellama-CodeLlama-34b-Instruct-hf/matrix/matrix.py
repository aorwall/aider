class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for row in matrix_string.splitlines():
            self.matrix.append(row.split())

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [row[index] for row in self.matrix]