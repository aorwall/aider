def recite(start, take=1):
    if start < 0:
        raise ValueError("Negative starting values are not allowed")
    elif start == 0:
        return "No more bottles of beer on the wall, no more bottles of beer."

    verses = []
    for i in range(take):
        num_bottles = start - i

        # Handle pluralization of "bottle"
        bottle_suffix = "" if num_bottles == 1 else "s"

        # Build first line of verse
        verse = f"{num_bottles} bottle{bottle_suffix} of beer on the wall, {num_bottles} bottle{bottle_suffix} of beer.\n"

        # Build second line of verse
        action = "it" if num_bottles == 1 else "one"
        next_num_bottles = num_bottles - 1 if num_bottles > 0 else 99
        next_bottle_suffix = "" if next_num_bottles == 1 else "s"
        verse += f"Take {action} down and pass it around, {next_num_bottles} bottle{next_bottle_suffix} of beer on the wall.\n"

        verses.append(verse)

    return "\n".join(verses) + "\n"
