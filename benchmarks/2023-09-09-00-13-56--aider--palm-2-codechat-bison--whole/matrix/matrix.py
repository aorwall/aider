class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = []
        self.columns = []

    def row(self, index):
        if index < 0 or index >= len(self.rows):
            raise ValueError("Invalid row index")
        return self.rows[index]

    def column(self, index):
        if index < 0 or index >= len(self.columns):
            raise ValueError("Invalid column index")
        return self.columns[index]

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def __str__(self):
        return self.matrix_string


def main():
    matrix_string = input("Enter a matrix of numbers, separated by spaces: ")
    matrix = Matrix(matrix_string)
    rows = matrix.get_rows()
    columns = matrix.get_columns()
    print("Rows:")
    for row in rows:
        print(row)
    print("Columns:")
    for column in columns:
        print(column)


if __name__ == "__main__":
    main()
