import collections
from concurrent.futures import ThreadPoolExecutor
def calculate(text_input):
    def count_letters(text):
        return dict(collections.Counter(text))

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(count_letters, text_input))

    final_result = collections.defaultdict(int)
    for result in results:
        for key, value in result.items():
            if key.isalpha(): # only consider alphabetic characters
                final_result[key.lower()] += value

    return dict(final_result)
