from typing import List

def can_chain(dominoes: List[List[int]]) -> List[List[int]]:
    domino_numbers = set()
    for domino in dominoes:
        domino_numbers.add(domino[0]) 
        domino_numbers.add(domino[1])

    if len(domino_numbers) > len(dominoes):
        return []

    seen = set()
    stack = []

    for domino in dominoes:
        if domino[0] not in seen:
            seen.add(domino[0])
            stack.append(domino)
            break

    while stack:
        current = stack[-1]
        if current[1] in seen:
            seen.add(current[1])
            if len(seen) == len(domino_numbers):
                return dominoes
            stack.pop()
        else:
            for domino in dominoes:
                if domino[0] == current[1]:
                    seen.add(domino[0])
                    stack.append(domino)
                    break
            else:
                return []
    return []
