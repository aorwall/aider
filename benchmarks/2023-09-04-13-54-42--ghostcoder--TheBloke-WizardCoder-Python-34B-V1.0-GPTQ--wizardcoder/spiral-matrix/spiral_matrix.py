from itertools import cycle

def spiral_matrix(size):
    if not (isinstance(size, int) and size > 0):
        raise ValueError("Size must be a positive integer")

    matrix = [[0] * size for _ in range(size)]
    directions = cycle([(0, -1), (-1, 0), (0, 1), (1, 0)])
    x, y = 0, 0
    direction = next(directions)
    value = 1

    while True:
        dx, dy = direction

        if 0 <= x + dx < size and 0 <= y + dy < size and matrix[y + dy][x + dx] == 0:
            x += dx
            y += dy
            matrix[y][x] = value
            value += 1

            if value > size ** 2:
                break

        else:
            direction = next(directions)

    return matrix
