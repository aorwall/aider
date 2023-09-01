def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    result = []
    for i in range(row_count):
        result.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                result[i].append(1)
            else:
                result[i].append(result[i-1][j-1] + result[i-1][j])
    return result


class PascalsTriangleTest(unittest.TestCase):
    def test_solution_is_recursive(self):
        with self.assertRaises(RecursionError):
            rows(1000)


if __name__ == '__main__':
    unittest.main()