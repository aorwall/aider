from collections import Counter

def best_hands(hands):
    def hand_rank(hand):
        ranks = sorted(card[0] for card in hand)
        suits = set(card[1] for card in hand)
        counts = Counter(card[0] for card in hand)

        if len(suits) == 1:
            if ranks == ['A', 'K', 'Q', 'J', 'T']:
                return (9,)
            elif ranks == ['A', 'A', 'K', 'K', 'Q']:
                return (8,)
            elif ranks == ['A', 'A', 'A', 'K', 'K']:
                return (7,)
            elif ranks == ['A', 'A', 'A', 'A', 'K']:
                return (6,)
            elif ranks == ['A', 'A', 'A', 'A', 'A']:
                return (5,)
            elif ranks[-1] == 'T':
                return (4, ranks)
            elif ranks[-1] == 'J':
                return (3, ranks)
            elif ranks[-1] == 'K':
                return (2, ranks)
            elif ranks[-1] == 'Q':
                return (1, ranks)
            else:
                return (0, ranks)
        else:
            if counts[ranks[-1]] == 4:
                return (8, ranks)
            elif counts[ranks[-1]] == 3:
                if counts[ranks[-2]] == 2:
                    return (7, ranks)
                elif ranks[-2] == ranks[-3]:
                    return (6, ranks)
                else:
                    return (5, ranks)
            elif counts[ranks[-1]] == 2:
                if counts[ranks[-2]] == 2:
                    return (4, ranks)
                else:
                    return (3, ranks)
            else:
                return (0, ranks)

    return [hand for hand in hands if hand_rank(hand) == max(hand_rank(hand) for hand in hands)]
