def roman(number):
    roman_numeral = ""
    
    if number < 1:
        return "Input must be a positive integer"
        
    digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    for i in range(len(digits)):
        count = int(number / digits[i])
        number -= count * digits[i]
        roman_numeral += numerals[i] * count
        
    return roman_numeral
