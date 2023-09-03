class PascalTriangle:
    def __init__(self, row_count):
        self.row_count = row_count

    @property
    def triangle(self):
        return [[1]] + self._generate_pascal_triangle()

    def _generate_pascal_triangle(self):
        prev_row = [1]
        for i in range(1, self.row_count):
            current_row = [(prev_row[j-1] + prev_row[j]) for j in range(i+1)]
            yield current_row
            prev_row = current_row

def rows(row_count):
    """Returns the first n rows of Pascal's Triangle"""
    if row_count < 0:
        raise ValueError("Number of rows cannot be negative.")
    elif row_count == 0:
        return []
    else:
        pt = PascalTriangle(row_count)
        return list(pt.triangle)
