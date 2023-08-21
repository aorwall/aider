def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    # Define the words for numbers from 0 to 19
    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    
    # Define the words for tens from 20 to 90
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    # Define the words for scales
    scales = [
        "", "thousand", "million", "billion"
    ]
    
    # Helper function to convert a number less than 1000 to words
    def convert_less_than_thousand(num):
        words = []
        
        # Convert the hundreds place
        if num >= 100:
            words.append(ones[num // 100])
            words.append("hundred")
            num %= 100
        
        # Convert the tens place
        if num >= 20:
            words.append(tens[num // 10])
            num %= 10
        
        # Convert the ones place
        if num > 0:
            words.append(ones[num])
        
        return words
    
    # Handle the case of 0 through 99
    if number < 100:
        return " ".join(convert_less_than_thousand(number))
    
    # Break the number up into chunks of thousands
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000
    
    # Convert each chunk to words and add the appropriate scale word
    words = []
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            words.extend(convert_less_than_thousand(chunk))
            words.append(scales[i])
    
    # Reverse the words list and join them with spaces
    words.reverse()
    return " ".join(words)