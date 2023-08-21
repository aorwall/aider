def find_anagrams(word, candidates):
    target = sorted(word.lower())
    return [candidate for candidate in candidates if sorted(candidate.lower()) == target and candidate.lower() != word.lower()]
