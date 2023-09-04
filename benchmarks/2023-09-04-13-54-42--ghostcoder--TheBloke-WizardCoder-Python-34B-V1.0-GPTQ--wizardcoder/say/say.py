import math
try:
    from num2words import num2words
except ModuleNotFoundError:
    def num2words(*args, **kwargs):
        raise NotImplementedError("Please install the required package: num2words.")
from num2words import num2words

def say(number):
    if not (0 <= number <= 9999999999999):
        raise ValueError("Input out of range")

    words = []
    chunks = split_into_chunks(number)
    for i, chunk in enumerate(chunks):
        chunk_words = num2words(chunk, lang='en', to='cardinal')

        # Add scale word if needed
        if i != len(chunks)-1:
            scale_word = get_scale_word(len(chunks)-i)
            chunk_words += f" {scale_word}"

        words.append(chunk_words)

    result = ' '.join(words)
    print(result)

def split_into_chunks(num):
    chunks = []
    while num > 0:
        chunks.insert(0, num % 1000)
        num //= 1000
    return chunks

def get_scale_word(power):
    scales = ["", "thousand", "million", "billion"]
    return scales[power]

if __name__ == "__main__":
    try:
        number = int(input())
        say(number)
    except ValueError as ve:
        print(ve)
