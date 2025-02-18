import collections
from multiprocessing import Pool

def count_letters(text):
    return dict(collections.Counter(text))

def calculate(text_input):
    pool = Pool()
    results = pool.map(count_letters, text_input)

    combined_results = collections.defaultdict(int)
    for single_result in results:
        for key, value in single_result.items():
            combined_results[key] += value

    return dict(combined_results)
