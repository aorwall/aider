def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    def combination(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return combination(n - 1, k - 1) + combination(n - 1, k)

    def pascal_row(n):
        return [combination(n, k) for k in range(n + 1)]

    triangle = []
    for i in range(row_count):
        row = pascal_row(i)
        triangle.append(row)

    return triangle
