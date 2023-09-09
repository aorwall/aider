def recite(start, take=1):
  lyrics = []

  for i in range(take):
    bottle_number = start - i

    if bottle_number > 2:
      lyrics.append(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
      lyrics.append(f"Take one down and pass it around, {bottle_number-1} bottles of beer on the wall.")
    elif bottle_number == 2:
      lyrics.append(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
      lyrics.append(f"Take one down and pass it around, {bottle_number-1} bottle of beer on the wall.")
    elif bottle_number == 1:
      lyrics.append(f"1 bottle of beer on the wall, 1 bottle of beer.")
      lyrics.append(f"Take it down and pass it around, no more bottles of beer on the wall.")
    else:
      lyrics.append(f"No more bottles of beer on the wall, no more bottles of beer.")
      lyrics.append(f"Go to the store and buy some more, 99 bottles of beer on the wall.")

  return lyrics
