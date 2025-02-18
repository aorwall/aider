from typing import List

def build_gift_list(day: int) -> List[str]:
    gifts = {
        12: "twelve Drummers Drumming",
        11: "eleven Pipers Piping",
        10: "ten Lords-a-Leaping",
         9: "nine Ladies Dancing",
         8: "eight Maids-a-Milking",
         7: "seven Swans-a-Swimming",
         6: "six Geese-a-Laying",
         5: "five Gold Rings",
         4: "four Calling Birds",
         3: "three French Hens",
         2: "two Turtle Doves",
         1: "one Partridge in a Pear Tree"
    }

    if day not in gifts:
        raise ValueError("Invalid day")

    return [gifts[day]]

def build_verse(day: int) -> str:
    gift_list = build_gift_list(day)
    first_line = f"On the {ordinal(day)} day of Christmas my true love gave to me:"
    gifts_str = ", ".join(gift_list)
    last_line = f"{first_line} {gifts_str}."
    return last_line

def ordinal(num: int) -> str:
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    if 1 <= num % 100 <= 20:
        return f"{num}th"
    else:
        return f"{num}{suffixes.get(num % 10, 'th')}"

def recite(start_verse: int, end_verse: int) -> List[str]:
    return [build_verse(i) for i in range(start_verse, end_verse+1)]

if __name__ == "__main__":
    print("\n".join(recite(1, 12)))