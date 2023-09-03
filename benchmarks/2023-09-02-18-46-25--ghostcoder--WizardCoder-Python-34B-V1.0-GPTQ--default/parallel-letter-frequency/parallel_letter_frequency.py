import concurrent.futures
from collections import Counter
import os

def calculate(text_list):
    def count_letters(chunk):
        return Counter(''.join(chunk))

    # Split the input text into equal-size chunks
    num_chunks = os.cpu_count()
    chunk_size = len(text_list) // num_chunks
    extra = len(text_list) % num_chunks
    chunks = [text_list[i * chunk_size:(i + 1) * chunk_size] if i < num_chunks - 1 else text_list[i * chunk_size + extra:] for i in range(num_chunks)]

    with ThreadPoolExecutor() as executor:
        counts = list(executor.map(count_letters, chunks))

    total_counter = sum(counts, Counter())
    return dict(total_counter)