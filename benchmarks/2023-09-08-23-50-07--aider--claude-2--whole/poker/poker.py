def best_hands(hands):
    """
    Given a list of poker hands, return a list of the best hand(s).
    """
    
    values = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    suits = 'H D C S'.split()
    
    def parse_hand(hand):
        """Parse a hand into a tuple of (rank, suit)"""
        cards = hand.split()
        return (values.index(cards[0]), suits.index(cards[1]))
    
    def hand_rank(hand):
        """Return a rank for the hand. Higher is better."""
        
        ranks = [parse_hand(h) for h in hand]
        
        # Check for flushes
        if len(set(s for r,s in ranks)) == 1:
            return (8, max(r for r,s in ranks))
        
        # Check for straights
        ranks = sorted(r for r,s in ranks)
        if ranks == list(range(ranks[0], ranks[0] + 5)):
            return (4, ranks[4])
        
        # Return high card
        return (0, ranks[4])
        
    # Rank all hands
    ranked_hands = [(hand_rank(hand), hand) for hand in hands]
    
    # Return best hand(s)
    return [hand for rank, hand in sorted(ranked_hands, reverse=True)]
