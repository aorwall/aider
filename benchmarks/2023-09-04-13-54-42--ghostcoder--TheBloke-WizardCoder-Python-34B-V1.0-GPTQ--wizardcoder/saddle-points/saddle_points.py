from typing import List, Tuple

def saddle_points(matrix: List[List[int]]) -> List[Tuple[int]]:
    # Check if the matrix is irregular
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    def find_max_and_min(index: int, values: list) -> Tuple[int]:
        max_value = max(values)
        min_value = min(values)

        if index == 0:
            return max_value, min_value
        else:
            return min_value, max_value

    saddle_points = []
    for i, row in enumerate(matrix):
        max_val, min_val = find_max_and_min(i % 2, row)
        for j, value in enumerate(row):
            if value == max_val and value == min_val:
                saddle_points.append((i, j))

    return saddle_points