def best_hands(hands):
  """
  Pick the best hand(s) from a list of poker hands.

  See https://en.wikipedia.org/wiki/List_of_poker_hands for an overview of poker hands.

  Args:
    hands: A list of poker hands, each represented as a list of cards.

  Returns:
    A list of the best hands, in decreasing order of rank.
  """

  # Sort the hands by rank.
  hands.sort(key=lambda hand: poker_hand_rank(hand))

  # Return the best hands.
  return hands[:5]

def poker_hand_rank(hand):
  """
  Return the rank of a poker hand.

  See https://en.wikipedia.org/wiki/List_of_poker_hands for an overview of poker hands.

  Args:
    hand: A poker hand, represented as a list of cards.

  Returns:
    The rank of the hand.
  """

  # Check for a royal flush.
  if is_royal_flush(hand):
    return 1

  # Check for a straight flush.
  if is_straight_flush(hand):
    return 2

  # Check for a four of a kind.
  if is_four_of_a_kind(hand):
    return 3

  # Check for a full house.
  if is_full_house(hand):
    return 4

  # Check for a flush.
  if is_flush(hand):
    return 5

  # Check for a straight.
  if is_straight(hand):
    return 6

  # Check for a three of a kind.
  if is_three_of_a_kind(hand):
    return 7

  # Check for two pairs.
  if is_two_pairs(hand):
    return 8

  # Check for a pair.
  if is_pair(hand):
    return 9

  # Otherwise, it's a high card.
  return 10

def