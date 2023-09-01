import multiprocessing
def calculate(text_input):
    # Create a dictionary to store the letter frequencies
    letter_frequencies = {}

    # Create a process pool with the number of CPU cores
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    # Map the texts to the letter frequency calculation function
    results = pool.map(calculate_letter_frequency, text_input)

    # Reduce the results to a single dictionary
    for result in results:
        for letter, frequency in result.items():
            if letter not in letter_frequencies:
                letter_frequencies[letter] = 0
            letter_frequencies[letter] += frequency

    return letter_frequencies

def calculate_letter_frequency(text):
    # Create a dictionary to store the letter frequencies
    letter_frequencies = {}

    # Iterate over the letters in the text
    for letter in text:
        if letter.isalpha():
            if letter not in letter_frequencies:
                letter_frequencies[letter] = 0
            letter_frequencies[letter] += 1

    return letter_frequencies
