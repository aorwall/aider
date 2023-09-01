def find_anagrams(word, candidates):
    """
    Find the anagrams of a given word in a list of candidates.
    
    Args:
        word (str): The target word to find anagrams for.
        candidates (list[str]): The list of candidate words to search in.
    
    Returns:
        list[str]: The list of anagrams found in the candidates.
    """
    # Create a dictionary to store the letter counts of the target word
    target_letter_count = {}
    for letter in word:
        if letter not in target_letter_count:
            target_letter_count[letter] = 1
        else:
            target_letter_count[letter] += 1

    # Create a list to store the anagrams found
    anagrams = []

    # Iterate over the candidates and check if they are anagrams of the target word
    for candidate in candidates:
        # Create a dictionary to store the letter counts of the candidate word
        candidate_letter_count = {}
        for letter in candidate:
            if letter not in candidate_letter_count:
                candidate_letter_count[letter] = 1
            else:
                candidate_letter_count[letter] += 1

        # Check if the candidate word is an anagram of the target word
        if target_letter_count == candidate_letter_count:
            anagrams.append(candidate)

    return anagrams
