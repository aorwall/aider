def roman(number):
    numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    result = ""
    for value, numeral in sorted(numeral_map.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result
