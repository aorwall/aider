def best_hands(hands):
    suits = {'S': 0, 'H': 1, 'D': 2, 'C': 3}
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def card_value(card):
        try:
            return (values[card[0]] * 4) + suits[card[1]]
        except IndexError:
            print("Invalid card: ", card)
            return -1

    def hand_score(hand):
        return sum(card_value(card) for card in hand)

    hands_with_scores = [(hand, hand_score(hand)) for hand in hands]
    max_score = max(hand[1] for hand in hands_with_scores if hand[1] != -1)
    winners = [hand for hand, score in hands_with_scores if score == max_score and score != -1]

    return winners
