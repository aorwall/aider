def recite(start, take=1):
    """Recites the lyrics of the "99 Bottles of Beer" song starting at start."""
    if start < 1:
        raise ValueError("Start must be greater than zero")

    result = []
    current = max(start - take + 1, 1)
    while current <= start:
        line = f"{current} bottles of beer on the wall, {current} bottles of beer.\n"
        line += f"Take one down and pass it around, "
        next_num = current - 1 if current > 1 else 'no more'
        line += f"{next_num} bottles of beer on the wall.\n\n"
        result.append(line)
        current -= 1
    return result[:take]
