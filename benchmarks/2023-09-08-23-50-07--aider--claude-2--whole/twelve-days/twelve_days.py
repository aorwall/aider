GIFTS = [
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

DAYS = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]

def recite(start_verse, end_verse):
    lyrics = []
    for verse in range(start_verse, end_verse+1):
        lyric = f"On the {DAYS[verse-1]} day of Christmas my true love gave to me: "
        gifts = GIFTS[verse-1::-1] # reverse gifts
        gifts_lyric = ", ".join(gifts)
        lyric += gifts_lyric + "."
        lyrics.append(lyric)
    return lyrics
