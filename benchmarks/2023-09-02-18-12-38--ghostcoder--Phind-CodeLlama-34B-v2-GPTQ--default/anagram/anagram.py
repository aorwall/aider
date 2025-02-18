def find_anagrams(word, candidates):
    # Normalize the word by converting it to lowercase
    word = word.lower()

    # Create a sorted version of the word
    sorted_word = "".join(sorted(word))

    # Initialize an empty list to store the anagrams
    anagrams = []

    # Iterate over each candidate
    for candidate in candidates:
        # Normalize the candidate by converting it to lowercase
        candidate_lower = candidate.lower()

        # Skip if the candidate is equal to the original word
        if candidate_lower == word:
            continue

        # Create a sorted version of the candidate
        sorted_candidate = "".join(sorted(candidate_lower))

        # Check if the sorted candidate equals the sorted word
        if sorted_candidate == sorted_word:
            # If so, add the candidate (with its original case) to the anagrams list
            anagrams.append(candidate)

    # Return the anagrams list
    return anagrams
