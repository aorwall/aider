from collections import Counter

def find_anagrams(word, candidates):
    target = Counter(word.lower())

    def is_anagram(candidate):
        if len(target) != len(candidate):
            return False

        candidate_counter = Counter(candidate.lower())
        return all([k in candidate_counter and v == candidate_counter[k] for k, v in target.items()])

    return [candidate for candidate in candidates if is_anagram(candidate)]
