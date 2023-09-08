def find_anagrams(word, candidates):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_same_case(word1, word2):
        return word1.lower() == word2.lower()

    anagram_set = []
    for candidate in candidates:
        if is_anagram(word, candidate) and not is_same_case(word, candidate):
            anagram_set.append(candidate)

    return anagram_set
