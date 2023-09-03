from collections import Counter

def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    result = []

    for candidate in candidates:
        if len(candidate) == len(word):
            candidate_lower = candidate.lower()
            if word_sorted == sorted(candidate_lower):
                result.append(candidate)
    return result
