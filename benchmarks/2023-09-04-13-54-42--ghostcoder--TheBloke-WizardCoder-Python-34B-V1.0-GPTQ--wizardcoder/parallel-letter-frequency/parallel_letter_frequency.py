import concurrent.futures
from collections import Counter

def calculate(text_input):
    counter = Counter()

    # Split text into chunks for parallel processing
    chunk_size = len(text_input) // 4
    if chunk_size < 1000:
        chunk_size = 1000

    chunks = [text_input[i:i+chunk_size] for i in range(0, len(text_input), chunk_size)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {}
        for chunk in chunks:
            future = executor.submit(count_letters, chunk)
            futures[future] = chunk

        for future in concurrent.futures.as_completed(futures):
            try:
                counter += future.result()
            except Exception as e:
                print("Exception occurred during calculation of letters frequency: ", str(e))

    return dict(counter)

def count_letters(text):
    return Counter(text.lower().replace("\n",""))

if __name__ == "__main__":
    test_text = ["Hello World\n", "This is a Test\n", "Python is fun\n"]
    print(calculate(test_text))
