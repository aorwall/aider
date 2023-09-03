def modifier(stat_value):
    """Calculate ability modifier based on stat value."""
    return (stat_value - 10) // 2


class Character:
