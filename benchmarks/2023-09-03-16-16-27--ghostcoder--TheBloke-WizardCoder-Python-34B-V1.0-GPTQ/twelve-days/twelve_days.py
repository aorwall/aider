def recite(start_verse, end_verse):
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
            "eleventh", "twelfth"]
    gifts = ["a partridge in a pear tree.", "two turtle doves, ", "three french hens, ", "four calling birds, ", 
            "five golden rings, ", "six geese-a-laying, ", "seven swans-a-swimming, ", "eight maids-a-milking, ", 
            "nine ladies dancing, ", "ten lords-a-leaping, ", "eleven pipers piping, ", "twelve drummers drumming."]

    def get_gift_text(day):
        return "\n".join([f"{gifts[i].capitalize()}{', ' if i < len(gifts)-2 else ''}" for i in range(len(gifts) - day)])

    result = []
    for i in range(start_verse - 1, end_verse):
        result += [f"On the {days[i]} day of Christmas my true love gave to me:\n{get_gift_text(i)}\n"]
    return result
