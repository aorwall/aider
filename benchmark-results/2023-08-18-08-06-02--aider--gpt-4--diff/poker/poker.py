def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), kind(1, ranks))
    elif two_pair(ranks):
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):
        return (1, kind(2, ranks), kind(1, ranks))
    else:
        return (0, ranks)

def best_hands(hands):
    "From a list of poker hands, return the best hand(s)."
    return max(hands, key=hand_rank)
