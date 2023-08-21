def recite(start_verse, end_verse):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = f"On the {days[i]} day of Christmas my true love gave to me: "
        for j in range(i, -1, -1):
            if j == 0 and i != 0:
                verse += "and "
            verse += gifts[j]
        verses.append(verse)

    return verses