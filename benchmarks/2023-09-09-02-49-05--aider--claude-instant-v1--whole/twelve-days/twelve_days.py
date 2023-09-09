gifts = [
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

all_gifts = "and a Partridge in a Pear Tree"

def recite(start_verse, end_verse):
  verses = ""
  for verse in range(start_verse, end_verse+1):
    day = f"On the {verse} day of Christmas my true love gave to me: "
    gifts_list = gifts[(verse-1)-1::-1] 
    gifts = ", ".join(gifts_list)
    if verse < len(gifts):
      gifts += ", "
    gifts += all_gifts
    verses += day + gifts + "\n"
  return verses
