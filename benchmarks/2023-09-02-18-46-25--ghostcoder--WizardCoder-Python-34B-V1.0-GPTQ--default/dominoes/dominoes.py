def can_chain(dominoes):
    def find_matching_pairs(stones, num):
        matching_pairs = []
        for i, j in enumerate(stones):
            if j[0] == num:
                matching_pairs.append((i - 1, i))
            elif j[1] == num:
                matching_pairs.append((i - 1, i))
        return matching_pairs

    def backtrack(stones, path=[]):
        if len(path) == len(stones):
            return path + [path[0]]

        available_moves = find_matching_pairs(stones, stones[len(path)][-1]) if path else list(range(len(stones)))
        for move in available_moves:
            new_path = path + [move]
            if move not in path and all([stone not in new_path for stone in stones[move]]):
                result = backtrack(stones, new_path)
                if result:
                    return result
        return None

    # Remove duplicates from input set of dominoes
    unique_dominoes = set()
    for d in dominoes:
        a, b = sorted(d)
        unique_dominoes.add((a, b))

    # Convert to tuple list for indexing
    stones = [(a, b) for (a, b) in unique_dominoes]

    chain = backtrack(stones)
    if chain is None:
        return False
    else:
        return [stones[i] for i in chain]
