from collections import Counter
import itertools

def best_hands(hands):
    def get_rank(card):
        ranks = '23456789TJQKA'
        return ranks.index(card[0])

    def is_flush(cards):
        suits = set([suit for _, suit in cards])
        return len(suits) == 1

    def is_straight(ranks):
        return max(ranks) - min(ranks) == len(set(ranks)) - 1

    def has_pair(ranks):
        counts = Counter(ranks)
        return max(counts.values()) >= 2

    def has_two_pair(ranks):
        pairs = [k for k, v in Counter(ranks).items() if v >= 2]
        return len(pairs) >= 2

    def has_three_of_a_kind(ranks):
        counts = Counter(ranks)
        return max(counts.values()) >= 3

    def has_four_of_a_kind(ranks):
        counts = Counter(ranks)
        return max(counts.values()) >= 4

    def has_full_house(ranks):
        counts = Counter(ranks)
        values = sorted(list(counts.values()), reverse=True)
        return values[0] == 3 and values[-1] == 2

    def has_straight_flush(ranks, flush):
        return is_straight(ranks) and flush

    def has_royal_flush(ranks):
        return has_straight_flush(ranks, True) and min(ranks) == 10

    def evaluate_hand(hand):
        # split card into rank and suit
        cards = [(get_rank(card), card[1]) for card in hand]
        # sort cards by rank
        cards.sort()
        # group cards by rank
        grouped = []
        for r, g in itertools.groupby(cards, lambda x: x[0]):
            grouped.append((r, list(g)))
        # extract ranks and suits separately
        ranks, suits = zip(*grouped)
        # check for straight flush
        if has_straight_flush(ranks, is_flush(suits)):
            return (9, None)
        elif has_royal_flush(ranks):
            return (9, None)
        elif has_four_of_a_kind(ranks):
            return (8, max(Counter(ranks).keys()))
        elif has_full_house(ranks):
            return (7, None)
        elif has_flush(suits):
            return (6, None)
        elif has_straight(ranks):
            return (5, None)
        elif has_three_of_a_kind(ranks):
            return (4, max(Counter(ranks).keys()))
        elif has_two_pair(ranks):
            pairs = [k for k, v in Counter(ranks).items() if v >= 2]
            return (3, pairs)
        elif has_pair(ranks):
            return (2, max(Counter(ranks).keys()))
        else:
            return (1, max(ranks))

    # convert hands to tuples of (score, high card)
    scores = [evaluate_hand(hand) for hand in hands]
    # find highest score
    max_score = max(scores)[0]
    # filter only hands with highest score
    winners = [i for i, s in enumerate(scores) if s[0] == max_score]
    # break ties based on high card
    winner_hands = [hands[i] for i in winners]
    winner_highest = max([max(hand, key=lambda c: get_rank(c)) for hand in winner_hands])
    # return indices of winning hands
    return [i for i, h in enumerate(hands) if winner_highest in h]
