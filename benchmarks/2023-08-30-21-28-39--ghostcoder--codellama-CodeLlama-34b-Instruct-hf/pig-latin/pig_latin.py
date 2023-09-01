def translate(text):
    """
    Translate the given text to Pig Latin.
    
    :param text: The text to translate.
    :return: The translated text.
    """
    # Split the text into words
    words = text.split()

    # Iterate over each word and translate it to Pig Latin
    translated_words = []
    for word in words:
        # Check if the word starts with a vowel sound
        if word.startswith(("a", "e", "i", "o", "u")):
            # If so, add an "ay" sound to the end of the word
            translated_word = word + "ay"
        else:
            # If the word starts with a consonant sound, move it to the end of the word
            # and then add an "ay" sound to the end of the word
            consonant_sound = ""
            for char in word:
                if char.isalpha() and not char.isdigit():
                    consonant_sound += char
                else:
                    break
            translated_word = word[len(consonant_sound):] + consonant_sound + "ay"

        # Add the translated word to the list of translated words
        translated_words.append(translated_word)

    # Join the translated words into a single string and return it
    return " ".join(translated_words)
