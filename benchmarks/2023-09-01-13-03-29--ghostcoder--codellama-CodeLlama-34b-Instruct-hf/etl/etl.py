def transform(legacy_data):
    new_data = {}
    for letter, score in legacy_data.items():
        new_data[letter.lower()] = score
    return new_data
