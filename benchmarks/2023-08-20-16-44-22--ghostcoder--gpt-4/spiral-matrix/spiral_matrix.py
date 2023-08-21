def spiral_matrix(size):
    matrix = [[0]*size for _ in range(size)]
    num = 1
    for layer in range((size + 1) // 2):
        for ptr in range(layer, size - layer):  # Traverse right
            matrix[layer][ptr] = num
            num += 1
        for ptr in range(layer + 1, size - layer):  # Traverse down
            matrix[ptr][size - layer - 1] = num
            num += 1
        for ptr in range(layer + 1, size - layer):  # Traverse left
            matrix[size - layer - 1][-ptr - 1] = num
            num += 1
        for ptr in range(layer + 1, size - layer - 1):  # Traverse up
            matrix[-ptr - 1][layer] = num
            num += 1
    return matrix