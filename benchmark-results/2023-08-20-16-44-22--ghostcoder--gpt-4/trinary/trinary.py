def trinary(string):
    if not all(char in '012' for char in string):
        return 0
    try:
        return sum(int(char) * 3 ** i for i, char in enumerate(string[::-1]))
    except ValueError:
        return 0