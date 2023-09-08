def abbreviate(words):
    acronym = ""
    for word in words.split():
        if word[0].isalpha():
            acronym += word[0].upper()
    return acronym
