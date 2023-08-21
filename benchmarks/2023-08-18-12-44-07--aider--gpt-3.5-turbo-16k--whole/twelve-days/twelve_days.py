def recite(start_verse, end_verse):
    # List of gifts for each day
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and a Partridge in a Pear Tree.",
        "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
    ]

    # Generate the verses based on the start and end verse numbers
    verses = []
    for i in range(start_verse - 1, end_verse):
        day = i + 1
        if day == 1:
            ordinal_day = "first"
        elif day == 2:
            ordinal_day = "second"
        elif day == 3:
            ordinal_day = "third"
        elif day == 4:
            ordinal_day = "fourth"
        elif day == 5:
            ordinal_day = "fifth"
        elif day == 6:
            ordinal_day = "sixth"
        elif day == 7:
            ordinal_day = "seventh"
        elif day == 8:
            ordinal_day = "eighth"
        elif day == 9:
            ordinal_day = "ninth"
        elif day == 10:
            ordinal_day = "tenth"
        elif day == 11:
            ordinal_day = "eleventh"
        elif day == 12:
            ordinal_day = "twelfth"
        verse = f"On the {ordinal_day} day of Christmas my true love gave to me: {gifts[i]}"
        verses.append(verse)

    return verses
