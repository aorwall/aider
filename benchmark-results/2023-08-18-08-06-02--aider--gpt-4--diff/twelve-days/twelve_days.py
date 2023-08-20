def recite(start_verse, end_verse):
    gifts = [
        ('first', 'a Partridge in a Pear Tree'),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth', 'five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming')
    ]

    lyrics = []
    for i in range(start_verse - 1, end_verse):
        verse = f"On the {gifts[i][0]} day of Christmas my true love gave to me: "
        verse += ', '.join(gift for day, gift in gifts[i::-1])
        verse = verse.replace('a Partridge', 'and a Partridge') if i != 0 else verse
        verse += '.'
        lyrics.append(verse)

    return lyrics
