def recite(start_verse, end_verse):
    lyrics = ""
    animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    
    for i in range(start_verse, end_verse+1):
        current = animals[i-1]
        lyrics += f"I know an old lady who swallowed a {current}.\n"
        if i == 1:
            lyrics += "I don't know why she swallowed the fly. Perhaps she'll die.\n"
        else:
            for j in range(i-1, 0, -1):
                previous = animals[j-1]
                lyrics += f"She swallowed the {current} to catch the {previous}.\n"
            lyrics += "I don't know why she swallowed the fly. Perhaps she'll die.\n"
            
        if i < len(animals):
            lyrics += "\n"
            
    return [lyrics]
