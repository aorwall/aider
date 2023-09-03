def recite(start, take=1):
    if start < 0 or take <= 0:
        return ""
    verses = []

    for i in range(start - take + 1, max(0, start - take + 2)):
        if i > 0:
            line1 = f"{i} bottles of beer on the wall, {i} bottles of beer."
            line2 = "Take one down and pass it around, "
            line3 = f"{i-1} bottles of beer on the wall."
            verse = line1 + "\n" + line2 + line3
        else:
            line1 = "No more bottles of beer on the wall, no more bottles of beer."
            line2 = "Go to the store and buy some more, "
            line3 = f"{99} bottles of beer on the wall."
            verse = line1 + "\n" + line2 + line3

        verses.append(verse)

    return '\n'.join(verses)
