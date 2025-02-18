from collections import defaultdict

def can_chain(dominoes):
    # Create a dictionary to store all possible connections
    connections = defaultdict(list)

    for domino in dominoes:
        left, right = domino
        connections[left].append(right)
        connections[right].append(left)

    # Start by checking the first domino's left side
    start = dominoes[0][0]
    end = None

    while True:
        # If we reached the end, check if there's a connection to the start
        if len(connections[start]) > 0 and end != start:
            end = start
            break

        # Otherwise, move to the next available domino
        elif len(connections[end]) > 0:
            start = connections[end].pop()
        else:
            break

    # Check if we made a full circle
    if end == dominoes[0][0]:
        return True

    return False
