from multiprocessing import Pool
import string

def calculate(text_input):

    letter_counts = {letter: 0 for letter in string.ascii_lowercase}

    def count_letters(text):
        letter_counts_local = {letter: 0 for letter in string.ascii_lowercase}
        for letter in text.lower():
            if letter in letter_counts_local:
                letter_counts_local[letter] += 1
        return letter_counts_local

    pool = Pool()
    results = pool.map(count_letters, text_input)
    pool.close()
    pool.join()
        
    for result in results:
        for letter, count in result.items():
            letter_counts[letter] += count
            
    return letter_counts
