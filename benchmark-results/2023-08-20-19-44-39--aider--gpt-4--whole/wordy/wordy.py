def answer(question):
    question = question.replace("What is ", "").replace("?", "")
    parts = question.split()

    if len(parts) % 2 == 0:
        raise ValueError("syntax error")

    try:
        result = int(parts[0])
    except ValueError:
        raise ValueError("syntax error")

    i = 1
    while i < len(parts):
        operator = parts[i]
        if operator == "multiplied" or operator == "divided":
            operator += " " + parts[i + 1]
            i += 1

        try:
            number = int(parts[i + 1])
        except ValueError:
            raise ValueError("syntax error")

        if operator == "plus":
            result += number
        elif operator == "minus":
            result -= number
        elif operator == "multiplied by":
            result *= number
        elif operator == "divided by":
            if number == 0:
                raise ValueError("division by zero")
            result //= number
        else:
            raise ValueError("unknown operation")

        i += 2

    return result
