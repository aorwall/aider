def recite(start_verse=1, end_verse=12):
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gifts = {0: "", 1: "a Partridge in a Pear Tree.", 2: "two Turtle Doves, ", 3: "three French Hens, ",
             4: "four Calling Birds, ", 5: "five Gold Rings, ", 6: "six Geese-a-Laying, ",
             7: "seven Swans-a-Swimming, ", 8: "eight Maids-a-Milking, ", 9: "nine Ladies Dancing, ",
             10: "ten Lords-a-Leaping, ", 11: "eleven Pipers Piping, ", 12: "twelve Drummers Drumming"}

    verses = []
    for day in range(start_verse - 1, end_verse):
        verse = f"On the {days[day]} day of Christmas my true love gave to me: " \
                + ''.join([gifts[i] if i <= day+1 else "" for i in range(1, len(gifts))])
        verses.append(verse)

    return verses