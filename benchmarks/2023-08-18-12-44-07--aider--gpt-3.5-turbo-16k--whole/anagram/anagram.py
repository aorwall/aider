def find_anagrams(word, candidates):
    anagrams = []
    target = sorted(word.lower())
    
    for candidate in candidates:
        if sorted(candidate.lower()) == target and candidate.lower() != word.lower():
            anagrams.append(candidate)
    
    return anagrams
