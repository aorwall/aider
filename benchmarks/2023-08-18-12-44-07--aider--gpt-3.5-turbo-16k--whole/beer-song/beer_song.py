def recite(start, take=1):
    lyrics = []
    for i in range(start, start - take, -1):
        if i > 2:
            lyrics.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            lyrics.append(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        elif i == 2:
            lyrics.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            lyrics.append(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
        elif i == 1:
            lyrics.append(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            lyrics.append("Take it down and pass it around, no more bottles of beer on the wall.")
        else:
            lyrics.append("No more bottles of beer on the wall, no more bottles of beer.")
            lyrics.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return lyrics
