def answer(question):
    words = question.replace('?', '').split()
    if words[0:2] != ['What', 'is'] or len(words) < 3:
        raise ValueError("syntax error")

    try:
        result = int(words[2])
    except ValueError:
        raise ValueError("syntax error")

    i = 3
    while i < len(words):
        operation = words[i]
        if operation == 'plus':
            if i+1 >= len(words):
                raise ValueError("syntax error")
            try:
                result += int(words[i+1])
            except ValueError:
                raise ValueError("syntax error")
        elif operation == 'minus':
            if i+1 >= len(words):
                raise ValueError("syntax error")
            try:
                result -= int(words[i+1])
            except ValueError:
                raise ValueError("syntax error")
        elif operation == 'multiplied':
            if i+2 >= len(words) or words[i+1] != 'by':
                raise ValueError("syntax error")
            try:
                result *= int(words[i+2])
            except ValueError:
                raise ValueError("syntax error")
            i += 1
        elif operation == 'divided':
            if i+2 >= len(words) or words[i+1] != 'by':
                raise ValueError("syntax error")
            try:
                result //= int(words[i+2])
            except ValueError:
                raise ValueError("syntax error")
            i += 1
        else:
            raise ValueError("syntax error")
        i += 2

    return result