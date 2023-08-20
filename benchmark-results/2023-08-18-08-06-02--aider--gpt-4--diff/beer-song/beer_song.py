def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i == 0:
            verses.append(["No more bottles of beer on the wall, no more bottles of beer.",
                           "Go to the store and buy some more, 99 bottles of beer on the wall."])
        elif i == 1:
            verses.append(["1 bottle of beer on the wall, 1 bottle of beer.",
                           "Take it down and pass it around, no more bottles of beer on the wall."])
        else:
            verses.append([f"{i} bottles of beer on the wall, {i} bottles of beer.",
                           f"Take one down and pass it around, {i-1} bottle{'s' if i-1 > 1 else ''} of beer on the wall."])
    return verses
