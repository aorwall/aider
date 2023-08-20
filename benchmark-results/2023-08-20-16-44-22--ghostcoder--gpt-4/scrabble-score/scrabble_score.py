def score(word, double_letter=None, triple_letter=None, double_word=False, triple_word=False):
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    word_score = 0
    for letter in word.upper():
        letter_score = letter_scores[letter]
        if letter == double_letter:
            letter_score *= 2
        elif letter == triple_letter:
            letter_score *= 3
        word_score += letter_score

    if double_word:
        word_score *= 2
    elif triple_word:
        word_score *= 3

    return word_score