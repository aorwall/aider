def say(number):
    if number == 0:
        return "zero"
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = ["", "thousand", "million", "billion"]
    digits = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
    }

    def english(n):
        if n < 20:
            return digits[n]
        elif n < 100:
            return digits[n // 10 * 10] + ("" if n % 10 == 0 else "-" + digits[n % 10])
        elif n < 1000:
            return digits[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + english(n % 100))

    parts = []
    for unit in units:
        if number % 1000 > 0:
            parts.append(english(number % 1000) + " " + unit)
        number //= 1000

    return " ".join(reversed(parts)).strip()
