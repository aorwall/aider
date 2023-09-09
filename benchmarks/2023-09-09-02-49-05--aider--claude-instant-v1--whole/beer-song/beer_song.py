def recite(start=99, take=1):
    verses = []
    
    for bottles in range(start, -1, -take):
        if bottles == 1:
            bottle = "bottle"
        else:
            bottle = "bottles"
            
        if bottles - take == 0:
            next_bottles = "no more"
        else:
            next_bottles = bottles - take
            
        verse = f"{bottles} {bottle} of beer on the wall, {bottles} {bottle} of beer."
        verses.append(verse)
        verse = f"Take one down and pass it around, {next_bottles} {bottle} of beer on the wall."
        verses.append(verse)
        
    if bottles == 0:
        last_verse = "No more bottles of beer on the wall, no more bottles of beer."
        verses.append(last_verse)
        last_verse = "Go to the store and buy some more, 99 bottles of beer on the wall."
        verses.append(last_verse)
        
    return "\n".join(verses)
