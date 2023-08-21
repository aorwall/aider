import concurrent.futures
import collections

def calculate(texts):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_letters, text) for text in texts]
        counts = collections.Counter()
        for future in concurrent.futures.as_completed(futures):
            counts.update(future.result())
    return counts

def count_letters(text):
    return collections.Counter(c.lower() for c in text if c.isalpha())
