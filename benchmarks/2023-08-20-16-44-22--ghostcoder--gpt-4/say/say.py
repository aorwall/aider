def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = ["", "thousand", "million", "billion"]
    nums = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def convert_hundreds(n):
        s = ""
        if n >= 100:
            s += nums[n // 100] + " hundred"
            n %= 100
            if n != 0:
                s += " "
        if n >= 20:
            s += tens[n // 10]
            n %= 10
            if n != 0:
                s += "-"
        if n >= 10:
            s += teens[n - 10]
            n = 0
        if n > 0:
            s += nums[n]
        return s

    if number == 0:
        return "zero"

    result = ""
    for unit in units:
        if number == 0:
            break
        number, n = divmod(number, 1000)
        word = convert_hundreds(n)
        if word:
            result = (word + " " + unit + " " + result).strip()
    return result