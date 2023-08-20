def transform(legacy_data):
    new_data = {}
    for point_value, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = point_value
    return new_data
