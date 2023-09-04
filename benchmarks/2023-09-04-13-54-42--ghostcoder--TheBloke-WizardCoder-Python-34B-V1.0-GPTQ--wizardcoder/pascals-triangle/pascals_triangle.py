from functools import lru_cache

@lru_cache()
def binomial(n, k):
    if k == 0 or n == k:
        return 1

    return binomial(n-1, k-1) + binomial(n-1, k)

def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    result = []

    for i in range(row_count):
        new_row = [binomial(i, j) for j in range(i+1)]
        result.append(new_row)
        prev_row = new_row

    return result
