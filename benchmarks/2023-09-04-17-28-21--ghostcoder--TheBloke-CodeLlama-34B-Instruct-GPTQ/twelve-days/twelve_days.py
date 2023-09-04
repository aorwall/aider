def recite(start_verse, end_verse):
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
        "twelfth",
    ]
    ordinals = [
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
        "twelfth",
    ]
    gifts = [
        "Partridge in a Pear Tree.",
        "Turtle Doves",
        "French Hens",
        "Calling Birds",
        "Gold Rings",
        "Geese-a-Laying",
        "Swans-a-Swimming",
        "Maids-a-Milking",
        "Ladies Dancing",
        "Lords-a-Leaping",
        "Pipers Piping",
        "Drummers Drumming",
    ]

    result = []
    for i in range(start_verse - 1, end_verse):
        line = f"On the {days[i]} day of Christmas my true love gave to me:"

        if i == 0:
            line += f"\n{gifts[-1]}"

        else:
            for j in reversed(range(int(ordinals[i]))):
                line += f"\n{j + 1} {gifts[j]},"

            line += f"\nand {gifts[-1]}"

        result.append(line)

    return "\n".join(result)
