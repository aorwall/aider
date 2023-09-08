def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000

    scale = ["", "thousand", "million", "billion", "trillion"]
    words = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        hundreds, tens, ones = chunk // 100, chunk // 10 % 10, chunk % 10
        if hundreds > 0:
            words.append(say(hundreds) + " hundred")
        if tens > 0 and ones == 0:
            words.append(["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][tens])
        if tens == 1:
            words.append(["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][ones])
        if tens != 1 and ones > 0:
            words.append(["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][ones])
        if i > 0:
            words.append(scales[i])

    result = " ".join(words)
    return result
