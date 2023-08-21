from collections import Counter
from multiprocessing import Pool

def count_letters(text):
    return Counter(char.lower() for char in text if char.isalpha())

def calculate(text_input):
    with Pool() as pool:
        counts = pool.map(count_letters, text_input)
    return sum(counts, Counter())