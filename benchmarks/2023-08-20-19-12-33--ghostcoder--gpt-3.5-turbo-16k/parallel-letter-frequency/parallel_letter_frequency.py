from multiprocessing import Pool

def calculate(text_input):
    # Create a dictionary to store the frequency of each letter
    frequency = {}

    # Iterate over each text in the input list
    for text in text_input:
        # Iterate over each character in the text
        for char in text:
            # Increment the count of the character in the frequency dictionary
            frequency[char] = frequency.get(char, 0) + 1

    return frequency

def parallel_calculate(text_input):
    # Create a pool of worker processes
    pool = Pool()

    # Split the text input into chunks for parallel processing
    chunk_size = len(text_input) // pool._processes
    chunks = [text_input[i:i+chunk_size] for i in range(0, len(text_input), chunk_size)]

    # Use the pool to calculate the frequency of letters in each chunk
    results = pool.map(calculate, chunks)

    # Merge the results from each chunk into a single frequency dictionary
    frequency = {}
    for result in results:
        for char, count in result.items():
            frequency[char] = frequency.get(char, 0) + count

    return frequency