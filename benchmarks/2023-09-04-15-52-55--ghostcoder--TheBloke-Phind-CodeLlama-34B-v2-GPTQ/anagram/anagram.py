from collections import Counter

def find_anagrams(target, candidates):
    target = target.lower()
    target_counter = Counter(target)

    anagrams = []
    for candidate in candidates:
        candidate_counter = Counter(candidate.lower())

        # Check if current candidate has the same character count as the target
        if target_counter == candidate_counter and target != candidate.lower():
            anagrams.append(candidate)

    return anagrams