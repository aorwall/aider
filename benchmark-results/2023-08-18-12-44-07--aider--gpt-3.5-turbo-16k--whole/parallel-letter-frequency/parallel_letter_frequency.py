from multiprocessing import Pool
from collections import Counter

# Function to count the frequency of letters in a single text
def count_letters(text):
    return Counter(text.lower())

def calculate(text_input):
    # Create a pool of worker processes
    pool = Pool()

    # Map the count_letters function to each text in the input list
    results = pool.map(count_letters, text_input)

    # Merge the results from all processes
    total_frequency = sum(results, Counter())

    return total_frequency
