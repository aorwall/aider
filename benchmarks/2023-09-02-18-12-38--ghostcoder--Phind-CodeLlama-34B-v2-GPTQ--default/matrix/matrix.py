class Matrix:
    def __init__(self, matrix_string):
        self._rows = []
        self._columns = []

        lines = matrix_string.strip().split('\n')
        for line in lines:
            row = list(map(int, line.split()))
            self._rows.append(row)

        transposed = list(zip(*lines))
        self._columns = [list(col) for col in transposed]

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns
