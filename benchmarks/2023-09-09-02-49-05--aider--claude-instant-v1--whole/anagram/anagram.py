from collections import Counter

def find_anagrams(word, candidates):
    word = word.lower()
    candidates = [candidate.lower() for candidate in candidates]
    
    word_counter = Counter(word)
    anagrams = []
    
    for candidate in candidates:
        candidate_counter = Counter(candidate)
        if word_counter == candidate_counter:
            anagrams.append(candidate)
            
    return anagrams
