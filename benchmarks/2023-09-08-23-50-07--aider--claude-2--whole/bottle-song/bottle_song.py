def recite(start, take=1):
  bottles = range(start, start-take, -1)

  song = []

  for i in bottles:
    if i == 10:
      verse = "Ten green bottles hanging on the wall,\n"
    elif i == 9:
      verse = "Nine green bottles hanging on the wall,\n" 
    elif i == 8:
      verse = "Eight green bottles hanging on the wall,\n"
    elif i == 7: 
      verse = "Seven green bottles hanging on the wall,\n"
    elif i == 6:
      verse = "Six green bottles hanging on the wall,\n"
    elif i == 5:
      verse = "Five green bottles hanging on the wall,\n" 
    elif i == 4:
      verse = "Four green bottles hanging on the wall,\n"
    elif i == 3:
      verse = "Three green bottles hanging on the wall,\n"
    elif i == 2:
      verse = "Two green bottles hanging on the wall,\n"
    elif i == 1:
      verse = "One green bottle hanging on the wall,\n"

    verse += f"{i} green bottle{'s' if i > 1 else ''} hanging on the wall,\n"

    if i > 1:
      verse += "And if one green bottle should accidentally fall,\n"
    elif i == 1:
      verse += "And if that green bottle should accidentally fall,\n"

    if i > 0:
      verse += f"There'll be {i-1} green bottle{'s' if i > 2 else ''} hanging on the wall.\n"

    song.append(verse)

  return '\n'.join(song)
