def score(word):
    scores = {
        ('AEIOULNRST',): 1,
        ('DG',): 2,
        ('BCMP',): 3,
        ('FHVWY',): 4,
        ('K',): 5,
        ('JX',): 8,
        ('QZ',): 10
    }

    # Calculate the score
    return sum(scores[key] for key in scores if all(c in key[0] for c in word))
