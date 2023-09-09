import itertools

def best_hands(hands):
    ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    hands_ranks = [[card[0] for card in hand] for hand in hands]
    best_hand = max(hands, key=lambda hand: poker_rank(hand))
    return best_hand

def poker_rank(hand):
    ranks = sorted([r for r in hand], reverse=True)
    for i in range(2,5):
        if ranks[0] == ranks[i]:
            ranks[i] = str(int(ranks[i])-1)
    rank_val = 0
    for i,r in enumerate(ranks):
        rank_val += ranks.index(r) * (len(ranks)**i)
    return rank_val
