def trinary(string):
    if any(c not in '012' for c in string):
        return 0
    return sum(int(c) * 3**i for i, c in enumerate(string[::-1]))
