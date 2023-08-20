def transform(legacy_data):
    return {letter.lower(): point for point, letters in legacy_data.items() for letter in letters}