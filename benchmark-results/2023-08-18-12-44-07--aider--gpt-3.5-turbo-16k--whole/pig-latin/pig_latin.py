def translate(text):
    # Split the text into words
    words = text.split()

    # List to store the translated words
    translated_words = []

    # Iterate over each word
    for word in words:
        # Check if the word starts with a vowel sound
        if word[0] in 'aeiou' or word[:2] in ['xr', 'yt']:
            # Rule 1: Add "ay" sound to the end of the word
            translated_word = word + 'ay'
        else:
            # Find the index of the first vowel in the word
            vowel_index = -1
            for i, char in enumerate(word):
                if char in 'aeiouy':
                    vowel_index = i
                    break

            # Check if the word starts with a consonant sound followed by "qu"
            if word[:vowel_index] == 'qu':
                # Rule 3: Move "qu" to the end of the word and add "ay" sound
                translated_word = word[vowel_index+1:] + word[:vowel_index+1] + 'ay'
            else:
                # Rule 2: Move the consonant sound to the end of the word and add "ay" sound
                translated_word = word[vowel_index:] + word[:vowel_index] + 'ay'

        # Add the translated word to the list
        translated_words.append(translated_word)

    # Join the translated words back into a single string
    translated_text = ' '.join(translated_words)

    return translated_text
