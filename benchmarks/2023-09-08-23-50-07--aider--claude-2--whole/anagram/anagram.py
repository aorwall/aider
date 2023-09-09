def find_anagrams(word, candidates):
    word = word.lower()
    anagrams = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower != word and sorted(candidate_lower) == sorted(word):
            anagrams.append(candidate)
    return anagrams
