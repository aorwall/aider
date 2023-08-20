def recite(start_verse, end_verse):
    days = [
        ('first', 'a Partridge in a Pear Tree.'),
        ('second', 'two Turtle Doves, and'),
        ('third', 'three French Hens,'),
        ('fourth', 'four Calling Birds,'),
        ('fifth', 'five Gold Rings,'),
        ('sixth', 'six Geese-a-Laying,'),
        ('seventh', 'seven Swans-a-Swimming,'),
        ('eighth', 'eight Maids-a-Milking,'),
        ('ninth', 'nine Ladies Dancing,'),
        ('tenth', 'ten Lords-a-Leaping,'),
        ('eleventh', 'eleven Pipers Piping,'),
        ('twelfth', 'twelve Drummers Drumming,')
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = f"On the {days[i][0]} day of Christmas my true love gave to me: "
        verse += ' '.join(gift for _, gift in reversed(days[:i+1]))
        verses.append(verse)

    return verses