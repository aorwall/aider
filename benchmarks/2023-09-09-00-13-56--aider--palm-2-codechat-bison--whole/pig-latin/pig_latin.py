def translate(text):
    words = text.split()
    translated_words = []
    for word in words:
        if word[0] in "aeiouAEIOU":
            translated_words.append(word + "ay")
        else:
            consonants = ""
            for letter in word:
                if letter not in "aeiouAEIOU":
                    consonants += letter
                else:
                    break
            translated_words.append(consonants + "ay" + word[len(consonants):])
    return " ".join(translated_words)
