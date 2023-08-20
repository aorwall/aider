import concurrent.futures
import collections

def count_letters(text):
    return collections.Counter(c.lower() for c in text if c.isalpha())

def calculate(text_input):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_letters, text) for text in text_input]
        counts = collections.Counter()
        for future in concurrent.futures.as_completed(futures):
            counts.update(future.result())
    return dict(counts)
