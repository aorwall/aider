def translate(text):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    def is_vowel(c):
        return c.lower() in vowels

    def is_consonant(c):
        return c.lower() in consonants

    def move_consonant_clusters(word):
        if len(word) > 1 and is_consonant(word[0]) and not is_vowel(word[1]):
            return word[1:] + word[0]
        return word

    def apply_rule_1(word):
        if is_vowel(word[0]):
            return word + "ay"
        return word

    def apply_rule_2(word):
        if not is_vowel(word[0]):
            return word[1:] + word[0] + "ay"
        return word

    def apply_rule_3(word):
        if len(word) > 1 and word[0] == "q" and word[1] == "u":
            return word[2:] + word[:2] + "ay"
        return word

    def apply_rule_4(word):
        if "y" in word.lower() and not (word.startswith("xr") or word.startswith("yt")):
            return word.replace("y", "ay")
        return word

    words = text.split(" ")
    translated_words = []

    for word in words:
        word = move_consonant_clusters(word)
        word = apply_rule_1(word)
        word = apply_rule_2(word)
        word = apply_rule_3(word)
        word = apply_rule_4(word)
        translated_words.append(word)

    return " ".join(translated_words)
