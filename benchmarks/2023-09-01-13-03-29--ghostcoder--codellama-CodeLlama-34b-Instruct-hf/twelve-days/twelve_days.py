def recite(start_verse, end_verse):
    verses = []
    for day in range(start_verse, end_verse + 1):
        verses.append(verse(day))
    return "\n".join(verses)

def verse(day):
    gifts = {
        1: "a Partridge in a Pear Tree.",
        2: "two Turtle Doves, and a Partridge in a Pear Tree.",
        3: "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        4: "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        5: "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        6: "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        7: "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        8: "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        9: "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        10: "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        11: "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
        12: "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
    }
    return "On the {} day of Christmas my true love gave to me: {}".format(ordinal(day), gifts[day])

def ordinal(n):
    if n in [11, 12, 13]:
        return "{}th".format(n)
    else:
        return {
            1: "first",
            2: "second",
            3: "third",
            4: "fourth",
            5: "fifth",
            6: "sixth",
            7: "seventh",
            8: "eighth",
            9: "ninth",
            10: "tenth",
        }[n]
