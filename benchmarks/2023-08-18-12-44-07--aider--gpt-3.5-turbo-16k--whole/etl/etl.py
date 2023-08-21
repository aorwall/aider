def transform(legacy_data):
    new_data = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = score
    return new_data
