def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = ["", "thousand", "million", "billion"]
    h_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if number == 0:
        return "zero"

    result = ""
    for unit in units:
        if number == 0:
            break

        number, n = divmod(number, 1000)
        if n == 0:
            continue

        hundreds, n = divmod(n, 100)
        tens, one = divmod(n, 10)

        words = []
        if hundreds > 0:
            words.append(ones[hundreds])
            words.append("hundred")
        if tens > 1:
            words.append(h_tens[tens - 2])
            if one > 0:
                words.append("-" + ones[one])
        elif tens == 1:
            words.append(teens[one])
        else:
            words.append(ones[one])

        if words:
            result = " ".join(words) + " " + unit + " " + result

    return result.strip()
