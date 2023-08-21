class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        rows = matrix_string.split('\n')
        for row in rows:
            self.matrix.append([int(num) for num in row.split()])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]