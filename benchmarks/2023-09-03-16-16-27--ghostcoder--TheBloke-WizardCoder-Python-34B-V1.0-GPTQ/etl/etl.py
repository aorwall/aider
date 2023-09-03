def transform(legacy_data):
    # Create a dictionary to hold all the scores
    scores = {}

    # Iterate over the keys (point values) in legacy_data
    for key in sorted(legacy_data.keys()):
        # Add each letter to the scores dictionary with its corresponding point value
        for letter in legacy_data[key].lower():
            scores[letter] = int(key)

    return scores
