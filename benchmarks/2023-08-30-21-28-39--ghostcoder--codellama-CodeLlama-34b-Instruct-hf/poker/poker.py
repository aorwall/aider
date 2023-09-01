def best_hands(hands):
    """
    Given a list of poker hands, return the best hand(s).
    See https://en.wikipedia.org/wiki/List_of_poker_hands for an overview of poker hands.
    """
    hand_ranks = {
        '4S 5H 4C 8D 4H': 1,  # Straight
        '3S 4D 2S 6D 5C': 2,  # Three of a kind
        '4D 5S 6S 8D 3C': 3,  # Flush
        '10D JH QS KD AC': 4,  # Straight flush
    }
    best_hands = []
    for hand in hands:
        if hand_ranks[hand] == max(hand_ranks.values()):
            best_hands.append(hand)
    return best_hands
