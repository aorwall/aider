import multiprocessing
from collections import Counter

def calculate(text_input):
    # Split text into smaller chunks
    chunk_size = max(len(text_input) // multiprocessing.cpu_count(), 1)
    chunks = (text_input[i : i + chunk_size] for i in range(0, len(text_input), chunk_size))

    # Create a process pool and map the chunks to processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_chunk, chunks)

    # Combine the results from each process
    combined_results = {}
    for result in results:
        for key, value in result.items():
            combined_results[key] = combined_results.get(key, 0) + value

    return combinedResults

def calculateChunk(chunk):
    counter = Counter()
    for char in chunk:
        counter[char] += 1
    return counter

def calculate_chunk(chunk):
    counter = Counter()
    for char in chunk:
        counter[char] += 1
    return counter
