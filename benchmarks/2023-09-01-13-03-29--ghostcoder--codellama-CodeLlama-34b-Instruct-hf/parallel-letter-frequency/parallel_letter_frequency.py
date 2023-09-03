import string
import multiprocessing as mp
def calculate(text_input):
    # Create a process pool with the number of CPU cores
    pool = mp.Pool(mp.cpu_count())

    # Split the input text into chunks
    chunks = [text_input[i::mp.cpu_count()] for i in range(mp.cpu_count())]

    # Map the chunks to the frequency calculation function
    results = pool.map(calculate_chunk, chunks)

    # Reduce the results to a single dictionary
    total_frequency = {}
    for result in results:
        for letter, frequency in result.items():
            if letter not in total_frequency:
                total_frequency[letter] = 0
            total_frequency[letter] += frequency

    return total_frequency

def calculate_chunk(chunk):
    # Remove punctuation and special characters from the input text
    chunk = chunk.translate(str.maketrans("", "", string.punctuation))

    # Calculate the frequency of each letter in the chunk
    frequency = {}
    for letter in chunk:
        if letter not in frequency:
            frequency[letter] = 0
        frequency[letter] += 1
    return frequency
