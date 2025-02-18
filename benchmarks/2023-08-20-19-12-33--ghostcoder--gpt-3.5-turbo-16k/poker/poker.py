def best_hands(hands):
    # Create a dictionary to map the rank of each hand
    rank_dict = {
        'High Card': 0,
        'One Pair': 1,
        'Two Pairs': 2,
        'Three of a Kind': 3,
        'Straight': 4,
        'Flush': 5,
        'Full House': 6,
        'Four of a Kind': 7,
        'Straight Flush': 8,
        'Royal Flush': 9
    }

    # Create a list to store the best hands
    best_hands = []

    # Initialize the maximum rank to -1
    max_rank = -1

    # Iterate through each hand
    for hand in hands:
        # Get the rank of the current hand
        rank = get_rank(hand)

        # If the rank of the current hand is greater than the maximum rank,
        # update the maximum rank and clear the list of best hands
        if rank_dict[rank] > max_rank:
            max_rank = rank_dict[rank]
            best_hands = [hand]
        # If the rank of the current hand is equal to the maximum rank,
        # append the current hand to the list of best hands
        elif rank_dict[rank] == max_rank:
            best_hands.append(hand)

    return best_hands


def get_rank(hand):
    # Split the hand into a list of cards
    cards = hand.split()

    # Create a dictionary to store the count of each card rank
    rank_count = {}

    # Iterate through each card
    for card in cards:
        # Get the rank of the current card
        rank = card[:-1]

        # If the rank is already in the dictionary, increment the count
        if rank in rank_count:
            rank_count[rank] += 1
        # Otherwise, add the rank to the dictionary with a count of 1
        else:
            rank_count[rank] = 1

    # Get the count of unique ranks
    unique_ranks = len(rank_count)

    # Get the count of each rank count
    count_count = {}
    for count in rank_count.values():
        if count in count_count:
            count_count[count] += 1
        else:
            count_count[count] = 1

    # Check for a straight
    is_straight = is_consecutive(cards)

    # Check for a flush
    is_flush = is_same_suit(cards)

    # Check for a straight flush
    is_straight_flush = is_straight and is_flush

    # Check for a royal flush
    is_royal_flush = is_straight_flush and 'A' in cards and 'K' in cards

    # Determine the rank of the hand
    if is_royal_flush:
        rank = 'Royal Flush'
    elif is_straight_flush:
        rank = 'Straight Flush'
    elif unique_ranks == 2 and 4 in count_count:
        rank = 'Four of a Kind'
    elif unique_ranks == 2 and 3 in count_count:
        rank = 'Full House'
    elif is_flush:
        rank = 'Flush'
    elif is_straight:
        rank = 'Straight'
    elif unique_ranks == 3 and 3 in count_count:
        rank = 'Three of a Kind'
    elif unique_ranks == 3 and 2 in count_count:
        rank = 'Two Pairs'
    elif unique_ranks == 4 and 2 in count_count:
        rank = 'One Pair'
    else:
        rank = 'High Card'

    return rank


def is_consecutive(cards):
    # Create a list to store the ranks of the cards
    ranks = []

    # Iterate through each card
    for card in cards:
        # Get the rank of the current card
        rank = card[:-1]

        # If the rank is 'A', append 14 to the list of ranks
        if rank == 'A':
            ranks.append(14)
        # If the rank is 'K', append 13 to the list of ranks
        elif rank == 'K':
            ranks.append(13)
        # If the rank is 'Q', append 12 to the list of ranks
        elif rank == 'Q':
            ranks.append(12)
        # If the rank is 'J', append 11 to the list of ranks
        elif rank == 'J':
            ranks.append(11)
        # If the rank is 'T', append 10 to the list of ranks
        elif rank == 'T':
            ranks.append(10)
        # Otherwise, append the integer value of the rank to the list of ranks
        else:
            ranks.append(int(rank))

    # Sort the list of ranks in ascending order
    ranks.sort()

    # Check if the ranks are consecutive
    for i in range(len(ranks) - 1):
        if ranks[i] + 1 != ranks[i + 1]:
            return False

    return True


def is_same_suit(cards):
    # Get the suit of the first card
    suit = cards[0][-1]

    # Check if all the cards have the same suit
    for card in cards:
        if card[-1] != suit:
            return False

    return True