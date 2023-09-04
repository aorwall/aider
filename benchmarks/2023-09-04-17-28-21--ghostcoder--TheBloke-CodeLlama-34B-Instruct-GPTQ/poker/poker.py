import itertools

def best_hands(hands):
    """Return the best hand(s) from a list of poker hands."""
    # Sort the hands by rank in descending order
    sorted_hands = sorted(hands, key=lambda x: get_rank(x), reverse=True)

    # Initialize the best hand(s) and their rank
    best_hands = []
    best_rank = -1

    # Iterate over each unique combination of hands
    for combination in itertools.combinations(sorted_hands, 5):
        rank = get_rank(combination)
        if rank > best_rank:
            best_hands = [combination]
            best_rank = rank
        elif rank == best_rank:
            best_hands.append(combination)

    return best_hands

def get_rank(hand):
    """Return the rank of a poker hand."""
    ranks = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]
    if len(set([card[0] for card in hand])) == 5:
        return ranks.index("Straight Flush")
    else:
        counts = [len([card for card in hand if card[0] == r]) for r in set([card[0] for card in hand])]
        if max(counts) >= 4:
            return ranks.index("Four of a Kind")
        elif max(counts) >= 3:
            return ranks.index("Full House")
        elif max(counts) >= 2:
            return ranks.index("Flush")
        else:
            return ranks.index("High Card")
