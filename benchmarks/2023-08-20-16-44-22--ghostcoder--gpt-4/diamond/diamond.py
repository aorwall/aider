def rows(letter):
    size = 2 * (ord(letter) - ord('A')) + 1
    diamond = [[' ' for _ in range(size)] for _ in range(size)]
    center = size // 2
    
    for row in range(size):
        for col in range(size):
            dist = max(abs(center - row), abs(center - col))
            if dist <= center:
                diamond[row][col] = chr(ord('A') + center - dist)
                diamond[row][size - col - 1] = chr(ord('A') + center - dist)
                diamond[size - row - 1][col] = chr(ord('A') + center - dist)
                diamond[size - row - 1][size - col - 1] = chr(ord('A') + center - dist)
    
    return [''.join(row) for row in diamond]