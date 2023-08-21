def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted_word and candidate.lower() != word.lower()]