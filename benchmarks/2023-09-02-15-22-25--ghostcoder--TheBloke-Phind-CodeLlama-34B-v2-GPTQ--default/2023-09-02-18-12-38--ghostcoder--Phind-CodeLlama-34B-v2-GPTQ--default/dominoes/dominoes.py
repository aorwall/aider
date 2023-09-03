def can_chain(dominoes):
    # Sort the dominos based on the LHS value
    sorted_dominoes = sorted(dominoes)

    n = len(sorted_dominoes)

    # Create a visited array to store the already used dominos
    visited = [False]*n

    # Start from the 0th domino as it has to be the starting point
    result = []

    if not _can_chain_util(sorted_dominoes, visited, 0, -1, result):
        return None

    return result + [result[0]]

def _can_chain_util(sorted_dominoes, visited, pos, prev, result):
    if pos == len(sorted_dominoes):
        # If we have reached the last domino and it matches with the first element in result
        if sorted_dominoes[pos][1] == result[0][0]:
            return True
        return False

    for i in range(len(sorted_dominoes)):
        # Check if this domino can be placed at the current position
        if not visited[i] and sorted_dominoes[i][1] == sorted_dominoes[pos][0]:
            # Mark this domino as visited and add it to the result
            visited[i] = True
            result.append(sorted_dominoes[i])

            # Recurse for the next position
            if _can_chain_util(sorted_dominoes, visited, pos+1, sorted_dominoes[i], result):
                return True

            # If placing this domino doesn't lead to a solution then remove it from the result
            visited[i] = False
            result.pop()

    return False
