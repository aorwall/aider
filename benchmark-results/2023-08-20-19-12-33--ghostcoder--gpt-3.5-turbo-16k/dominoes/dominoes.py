def normalize_dominoes(dominoes):
    if not dominoes:
        return []
    return list(sorted(tuple(sorted(domino)) for domino in dominoes))