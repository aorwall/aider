def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("Input out of range")

    # Define the mapping of numbers to words
    num_to_word = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    # Handle numbers from 0 to 20 directly
    if number <= 20:
        return num_to_word[number]

    # Handle numbers from 21 to 99
    tens = number // 10 * 10
    ones = number % 10
    return num_to_word[tens] + '-' + num_to_word[ones]
