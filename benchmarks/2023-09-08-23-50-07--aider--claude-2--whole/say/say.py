def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
        
    if number == 0:
        return "zero"

    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    result = ""

    if number < 10:
        result = ones[number-1]
    elif number < 20:
        result = teens[number-11]
    elif number < 100:
        result = tens[number//10] + "-" + ones[number%10-1] if number%10 != 0 else tens[number//10]
    elif number < 1000:
        result = ones[number//100-1] + " hundred" 
    elif number < 1000000:
        result = say(number//1000) + " thousand " + say(number%1000)
    elif number < 1000000000:
        result = say(number//1000000) + " million " + say(number%1000000)
    elif number < 1000000000000:
        result = say(number//1000000000) + " billion " + say(number%1000000000)
        
    return result.strip()
