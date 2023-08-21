def recite(start_verse, end_verse):
    gifts = [
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]

    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = f"On the {days[i]} day of Christmas my true love gave to me: "
        verse += ', '.join(gifts[i:0:-1])
        if i > 0:
            verse += ", and "
        verse += gifts[0]
        verse += "."
        verses.append(verse)

    return verses
