def int_to_roman(num):
    val = [
        1000, 900, 500, 400, 100,
        90, 50, 40, 10,
        9, 5, 4, 1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num



def roman(number):
    if not isinstance(number, int) or number < 1 or number > 39999:
        raise ValueError("Number must be an integer between 1 and 39999")
    else:
        return int_to_roman(number)

