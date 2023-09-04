import itertools
from collections import Counter

RANKS = "23456789TJQKA"
SUITS = "SHDC"

def card_value(card):
    rank_value = RANKS.index(card[0])
    suit_value = SUITS.index(card[1])
    return rank_value, suit_value

def flush(hand):
    suits = set(card[1] for card in hand)
    return len(suits) == 1

def straight(ranks):
    return (max(ranks) - min(ranks)) == 4 and len(set(ranks)) == 5

def kind(n, ranks):
    counts = Counter(ranks)
    return any(count == n for count in counts.values())

def two_pair(ranks):
    pairs = set()
    for rank, group in itertools.groupby(sorted(ranks)):
        if len(list(group)) >= 2:
            pairs.add(rank)
        if len(pairs) == 2:
            return True
    return False

def full_house(ranks):
    counts = Counter(ranks)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2

def four_of_a_kind(ranks):
    counts = Counter(ranks)
    return any(count == 4 for count in counts.values())

def three_of_a_kind(ranks):
    counts = Counter(ranks)
    return any(count == 3 for count in counts.values())

def best_hands(hands):
    def get_score(hand):
        cards = [(RANKS.index(card[0]), card[1]) for card in hand]
        ranks = [card[0] for card in cards]
        suites = [card[1] for card in cards]

        if flush(cards) and straight(ranks):
            return (8, max(ranks))
        elif kind(4, ranks):
            return (7, max(filter(lambda r: ranks.count(r) == 4, ranks)))
        elif kind(3, ranks) and kind(2, ranks):
            return (6, max(filter(lambda r: ranks.count(r) == 3, ranks)), max(filter(lambda r: ranks.count(r) == 2, ranks)))
        elif flush(cards):
            return (5, max(ranks), sorted(ranks)[-2:])
        elif straight(ranks):
            return (4, max(ranks))
        elif three_of_a_kind(ranks):
            return (3, max(filter(lambda r: ranks.count(r) == 3, ranks)), sorted(filter(lambda r: ranks.count(r) == 1, ranks))[::-1])
        elif two_pair(ranks):
            return (2, tuple(sorted(filter(lambda r: ranks.count(r) == 2, ranks), reverse=True)))
        else:
            return (1, sorted(ranks)[-2:])

    scores = [get_score(hand) for hand in hands]
    winner = max(enumerate(scores), key=lambda x: x[1])[0]
    return winner
