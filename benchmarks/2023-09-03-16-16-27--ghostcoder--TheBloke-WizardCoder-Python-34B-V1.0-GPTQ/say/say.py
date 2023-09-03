def say(number):
    # Define the dictionary mapping for single digits
    ones = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    # Define the dictionary mapping for double digits
    tens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    # Define the dictionary mapping for tens
    tens_multiples = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    # Define the dictionary mapping for thousands
    thousands = ["", "thousand", "million", "billion"]

    def num_to_words(num):
        """Converts a number less than 10000 into words"""
        if num == 0:
            return ""
        elif num < 10:
            return ones[num] + " "
        elif num < 20:
            return tens[num] + " "
        elif num < 100:
            return tens[(num // 10)] + " " + ones[num % 10] + " "
        else:
            return ones[(num // 100)] + " hundred " + num_to_words(num % 100)


    # Check if the input is out of range
    if number < 0 or number > 99999999999:
        raise ValueError("Input out of range")


    # Convert the number to string and split by groups of 3 digits
    num_str = str(number)
    num_groups = [int(num_str[i:i+3]) for i in range(0, len(num_str), 3)]

    # Initialize the result list
    result = []

    # Iterate over each group of digits starting from the least significant digit
    for i, group in enumerate(reversed(num_groups):
        # If the current group has leading zeros, skip it
        if group == 0:
            continue
        # Get the corresponding word for the group and add it to the result list
        result.append(num_to_words(group))
        # Add the name of the scale (thousands, millions, billions) if needed
        if i != 0 and group != 0:
            result.append(thousands[len(num_groups)-i-1])

    # Join the words using spaces and return the final result
    return ' '.join(result[: : :-1]).strip()
