from collections import Counter
import itertools

def card_rank(card):
    """Return the rank of a card."""
    return int(card[0]) if card[0] in '23456789' else {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1}[card[0]]

def card_suit(card):
    """Return the suit of a card."""
    return card[-1]

def is_straight(ranks):
    """Check if a list of ranks is a straight."""
    return len(set(ranks)) == len(ranks) and max(ranks)-min(ranks) == len(ranks)-1

def is_flush(cards):
    """Check if a list of cards is flush."""
    return len(set([card_suit(card) for card in cards])) == 1

def is_royal_flush(cards):
    """Check if a list of cards is a royal flush."""
    return is_straight([card_rank(card) for card in cards]) and is_flush(cards) and max(cards,key=card_rank)=='TC'

def get_hand_strength(hand):
    """Evaluate the strength of a hand."""
    ranks = [card_rank(card) for card in hand]
    if is_royal_flush(hand):
        return (9, )
    elif is_straight_flush(hand):
        return (8, max(ranks))
    elif is_four_of_a_kind(ranks):
        return (7, max(ranks))
    elif is_full_house(ranks):
        return (6, max(ranks))
    elif is_flush(hand):
        return (5, )
    elif is_straight(ranks):
        return (4, max(ranks))
    elif is_three_of_a_kind(ranks):
        return (3, max(ranks))
    elif is_two_pair(ranks):
        return (2, sorted(ranks)[-1], sorted(ranks)[-2])
    elif is_pair(ranks):
        return (1, max(ranks))
    else:
        return (0, max(ranks))

def compare_hands(hand1, hand2):
    """Compare two hands and return the winner."""
    strength1 = get_hand_strength(hand1)
    strength2 = get_hand_strength(hand2)
    if strength1 > strength2:
        return hand1
    elif strength2 > strength1:
        return hand2
    else:
        return None

def best_hands(hands):
    """Find the best hand among multiple hands."""
    assert len(hands) > 0
    if len(hands) == 1:
        return hands[0]
    else:
        pairs = [(compare_hands(h1, h2), h1, h2) for h1 in hands for h2 in hands if h1 < h2]
        return min((p[0] or p[1] for p in pairs), default=None)
