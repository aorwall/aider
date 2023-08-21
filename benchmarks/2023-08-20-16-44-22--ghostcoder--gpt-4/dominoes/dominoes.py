def can_chain(dominoes):
    if not dominoes:
        return None

    # Try to start the chain from each domino
    for i in range(len(dominoes)):
        chain = dfs(dominoes[:i] + dominoes[i+1:], [dominoes[i]])
        if chain:
            return chain

    return None

def dfs(remaining, chain):
    # If there are no remaining dominoes and the chain is valid, return the chain
    if not remaining and chain[0][0] == chain[-1][1]:
        return chain

    # Try to add each remaining domino to the chain
    for i in range(len(remaining)):
        domino = remaining[i]
        # If the domino can be added to the chain, add it and continue the search
        if chain[-1][1] == domino[0]:
            result = dfs(remaining[:i] + remaining[i+1:], chain + [domino])
            if result:
                return result
        # If the domino can be added to the chain in reverse order, add it and continue the search
        elif chain[-1][1] == domino[1]:
            result = dfs(remaining[:i] + remaining[i+1:], chain + [domino[::-1]])
            if result:
                return result

    # If no domino can be added to the chain, return None
    return None