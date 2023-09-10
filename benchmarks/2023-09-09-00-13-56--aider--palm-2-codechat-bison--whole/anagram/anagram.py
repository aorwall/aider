def find_anagrams(word, candidates):
    """
    Finds all anagrams of the given word in the list of candidates.

    Args:
        word: The word to find anagrams of.
        candidates: A list of words to search for anagrams in.

    Returns:
        A list of all anagrams of the given word in the list of candidates.
    """

    # Create a set of all the letters in the target word.
    letters = set(word)

    # Create a list of all the candidates that contain all of the letters in the target word.
    candidates = [c for c in candidates if all(letter in c for letter in letters)]

    # Sort each candidate in alphabetical order.
    candidates = sorted(candidates)

    # Create a dictionary that maps each candidate to its sorted form.
    candidates_map = {c: sorted(c) for c in candidates}

    # Return all of the candidates that are mapped to the sorted form of the target word.
    return [c for c in candidates_map if candidates_map[c] == sorted(word)]
