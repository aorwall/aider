def recite(start, take=1):
    lyrics = []
    for i in range(start, start - take, -1):
        if i > 2:
            lyrics.append(f"{i} green bottles hanging on the wall,")
            lyrics.append(f"{i} green bottles hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append(f"There'll be {i-1} green bottles hanging on the wall.")
        elif i == 2:
            lyrics.append(f"{i} green bottles hanging on the wall,")
            lyrics.append(f"{i} green bottles hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append(f"There'll be {i-1} green bottle hanging on the wall.")
        elif i == 1:
            lyrics.append(f"{i} green bottle hanging on the wall,")
            lyrics.append(f"{i} green bottle hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append("There'll be no green bottles hanging on the wall.")
    return lyrics