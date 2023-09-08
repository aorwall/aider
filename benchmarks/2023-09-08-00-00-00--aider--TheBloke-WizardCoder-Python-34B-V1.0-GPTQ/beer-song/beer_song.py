def recite(start, take_down):
    """
    Generate the lyrics for the beer song starting from the given number of bottles.

    Args:
        start (int): The starting number of bottles of beer.
        take_down (int): The number of bottles to take down in each iteration.

    Returns:
        str: The lyrics for the beer song.
    """
    lyrics = ""
    for i in range(start, -1, -take_down):
        current_bottles = i if i > 0 else "No more"
        lyrics += f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer.\n"
        lyrics += f"Take one down and pass it around, "
        lyrics += f"{i - take_down} bottles of beer on the wall.\n" if i - take_down > 0 else f"no more bottles of beer on the wall.\n"
        lyrics += "\n" if i - take_down > 0 else f"Go to the store and buy some more, {start - 1} bottles of beer on the wall.\n\n"
    return lyrics