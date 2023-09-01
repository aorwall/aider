def can_chain(dominoes):
    # Check if the input is valid
    if len(dominoes) == 0:
        return False

    # Initialize a list to store the chain of dominoes
    chain = []

    # Loop through the input dominoes and try to form a chain
    for i in range(len(dominoes)):
        # If the current domino is not in the chain, add it to the chain
        if dominoes[i] not in chain:
            chain.append(dominoes[i])
        # If the current domino is already in the chain, check if it can be extended
        else:
            # If the current domino can be extended, extend it
            if dominoes[i][1] == chain[-1][0]:
                chain.append(dominoes[i])
            # If the current domino cannot be extended, return False
            else:
                return False

    # If the chain is complete, return True
    if len(chain) == len(dominoes):
        return True
    # If the chain is not complete, return False
    else:
        return False