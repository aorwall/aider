from typing import List

def can_chain(dominoes: List[str]) -> bool:
    def find_next_domino(current_end: str, remaining_dominoes: List[str]) -> str:
        for domino in remaining_dominoes:
            if current_end in domino:
                remaining_dominoes.remove(domino)
                return domino
        return None

    def is_valid_chain(chain: List[str]) -> bool:
        if not chain:
            return True
        first, last = chain[0], chain[-1]
        return first.split("|")[0] == last.split("|")[1]

    chain = []
    current_domino = dominoes.pop(0)
    chain.append(current_domino)

    while dominoes:
        next_domino = find_next_domino(current_domino.split("|")[1], dominoes)
        if not next_domino:
            return False
        chain.append(next_domino)
        current_domino = next_domino

    return is_valid_chain(chain)

# Test cases
print(can_chain(["2|1", "2|3", "1|3"]))  # True
print(can_chain(["1|2", "4|1", "2|3"]))  # False
