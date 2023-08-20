def can_chain(dominoes):
    # Check if the given set of dominoes can form a valid domino chain
    # Return True if it is possible, False otherwise
    
    def backtrack(dominoes, chain):
        # Base case: if all dominoes have been used, check if the first and last numbers match
        if len(chain) == len(dominoes):
            if chain[0][0] == chain[-1][1]:
                return True
            else:
                return False
        
        # Try each domino in the remaining set
        for i in range(len(dominoes)):
            # If the domino is already used, skip it
            if dominoes[i] in chain:
                continue
            
            # If the chain is empty, add the first domino
            if len(chain) == 0:
                chain.append(dominoes[i])
                if backtrack(dominoes, chain):
                    return True
                chain.pop()
            
            # If the chain is not empty, check if the domino can be added
            else:
                if chain[-1][1] == dominoes[i][0]:
                    chain.append(dominoes[i])
                    if backtrack(dominoes, chain):
                        return True
                    chain.pop()
                elif chain[-1][1] == dominoes[i][1]:
                    chain.append((dominoes[i][1], dominoes[i][0]))
                    if backtrack(dominoes, chain):
                        return True
                    chain.pop()
        
        return False
    
    return backtrack(dominoes, [])
