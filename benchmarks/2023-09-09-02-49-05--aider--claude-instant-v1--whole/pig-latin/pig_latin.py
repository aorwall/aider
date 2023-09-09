def translate(text):

  words = text.split()
  pig_latin = []

  for word in words:
    vowel_sounds = ["a","e","i","o","u","xr","yt"]
    if word[0] in vowel_sounds:
      pig_latin.append(f"{word}ay")
    elif word[:2] == "qu":
      pig_latin.append(f"{word[2:]}{word[:2]}ay")
    elif word[0] in "bcdfghjklmnpqrstvwxyz":
      pig_latin.append(f"{word[1:]}{word[0]}ay")
    elif word[:1] in "bcdfghjklmnpqrstvwxyz" and word[1] == "y":
      pig_latin.append(f"{word[2:]}{word[:2]}ay")
    else:
      pig_latin.append(word)

  return " ".join(pig_latin)
