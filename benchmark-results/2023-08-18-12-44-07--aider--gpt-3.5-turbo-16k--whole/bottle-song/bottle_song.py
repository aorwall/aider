def recite(start, take=1):
    lyrics = []
    for i in range(start, start - take, -1):
        if i > 1:
            lyrics.append(f"{i} green bottles hanging on the wall,")
            lyrics.append(f"{i} green bottles hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append(f"There'll be {i-1} green bottles hanging on the wall.")
        elif i == 1:
            lyrics.append("One green bottle hanging on the wall,")
            lyrics.append("One green bottle hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append("There'll be no green bottles hanging on the wall.")
        else:
            lyrics.append("No green bottles hanging on the wall,")
            lyrics.append("No green bottles hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append("There'll be no green bottles hanging on the wall.")
        lyrics.append("")  # Add an empty line between verses

    return "\n".join(lyrics)
