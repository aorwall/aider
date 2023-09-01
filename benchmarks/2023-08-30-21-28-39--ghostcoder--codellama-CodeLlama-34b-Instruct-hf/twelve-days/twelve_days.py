def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse + 1):
        verses.append(verse(i))
    return "\n".join(verses)

def verse(n):
    gifts = ["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens", "four Calling Birds", "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]
    if n == 1:
        return "On the first day of Christmas my true love gave to me: " + gifts[0]
    elif n == 12:
        return "On the twelfth day of Christmas my true love gave to me: " + gifts[11]
    else:
        return "On the " + str(n) + "th day of Christmas my true love gave to me: " + ", ".join(gifts[:n])
