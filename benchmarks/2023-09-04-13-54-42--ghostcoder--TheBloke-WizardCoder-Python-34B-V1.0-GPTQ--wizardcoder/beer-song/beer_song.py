def recite(start, take=1):
    """Recites a portion of the beer song starting at start."""

    # Create a list of strings representing each line of the lyrics for the given verse
    lyrics = []
    if start >= 0:
        for i in range(take):
            current_verse = create_verse(start - i)
            lyrics += [current_verse] + ["\n"] * (i % 2 == 0)

    return "\n".join(lyrics).rstrip()

def create_verse(bottles):
    """Creates a single verse of the beer song with the given number of bottles."""

    if bottles < 0:
        return ""
    elif bottles == 0:
        return f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {abs(bottles)} bottles of beer on the wall."
    elif bottles == 1:
        return f"1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall."
    else:
        return f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\nTake one down and pass it around, {bottles-1} bottles of beer on the wall."

if __name__ == '__main__':
    print(recite(10))
