def can_chain(dominoes):
    # Sort the dominos based on their key, which is the string representation of the domino
    sorted_dominnoes = sorted(dominoes, key=lambda x: str(x[0]) + "|" + str(x[1]))

    # Check the edge case when there's only one domino
    if len(sorted_dominnoes) == 1:
        return True

    # Iterate over the sorted dominos
    for i in range(len(sorted_dominnoes)):

        # If we reach the last domino, break the loop
        if i == len(sorted_dominnoes) - 1:
            break

        current_domino = sorted_dominnoes[i]
        next_domino = sorted_dominnoes[i + 1]

        # If the current domino's right value doesn't equal the next domino's left value, return False
        if current_domino[1] != next_domino[0]:
            return False

    # After iterating over all dominos, if no mismatch found, return True
    return True
