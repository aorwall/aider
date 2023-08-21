def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    return [candidate for candidate in candidates if sorted_word == sorted(candidate.lower()) and word_lower != candidate.lower()]
