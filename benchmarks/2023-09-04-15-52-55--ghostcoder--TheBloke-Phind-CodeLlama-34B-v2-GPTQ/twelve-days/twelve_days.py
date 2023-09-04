def recite(start_verse, end_verse):
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gifts = {12: 'Drummers Drumming', 11: 'Pipers Piping', 10: 'Lords-a-Leaping', 9: 'Ladies Dancing', 8: 'Maids-a-Milking', 7: 'Swans-a-Swimming', 6: 'Geese-a-Laying', 5: 'Gold Rings', 4: 'Calling Birds', 3: 'French Hens', 2: 'Turtle Doves', 1: 'Partridge in a Pear Tree'}

    result = []
    for i in range(end_verse - start_verse + 1):
        verse = f"On the {days[(i+start_verse)-1]} day of Christmas my true love gave to me:"
        for j in reversed(range(1, (i+start_verse)+1)):
            if (j < len(gifts)) :
                verse += f" {gifts[j]}"
            else:
                break
            if j > 1:
                verse += ","
            else:
                verse += " and a "

        result.append(verse)

    return result # Changed from '\n'.join(result) as we want list instead of string
