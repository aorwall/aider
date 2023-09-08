from collections import Counter
from concurrent.futures import ThreadPoolExecutor

def calculate(text_input):
    with ThreadPoolExecutor() as executor:
        total_frequency = sum(executor.map(Counter, text_input), Counter())
    return total_frequency
