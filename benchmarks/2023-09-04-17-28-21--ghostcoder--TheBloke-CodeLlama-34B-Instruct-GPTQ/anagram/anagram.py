import itertools

def find_anagrams(target, candidates):
    """Return the list of anagrams of 'target' among 'candidates'"""
    # Sort each word to normalize their letter order
    sorted_target = "".join(sorted(target))
    sorted_candidates = ["".join(sorted(w)) for w in candidates]

    # Find the anagrams by comparing the sorted words
    anagrams = []
    for cand in sorted_candidates:
        if cand == sorted_target and target != cand:
            anagrams.append(cand)

    # Return the original unsorted words
    return [w for w in candidates if "".join(sorted(w)) in anagrams]