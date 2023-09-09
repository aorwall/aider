from multiprocessing import Pool
import pickle

def count_letters(text):
    letters = "abcdefghijklmnopqrstuvwxyz"

    count = [0] * len(letters)
    for char in text.lower():
        if char in letters:
            count[letters.index(char)] += 1
    return count

def calculate(text_input):

    with Pool() as p:
        counts = p.map(count_letters, text_input)

    total = [0] * 26
    for count in counts:
        for i in range(26):
            total[i] += count[i]

    return total
