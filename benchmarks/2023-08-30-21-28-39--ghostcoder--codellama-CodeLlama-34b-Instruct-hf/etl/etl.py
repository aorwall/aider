import json
def transform(legacy_data):
    letters = json.loads(json.dumps(legacy_data))
    new_data = {}
    for letter, score in letters.items():
        new_data[letter.lower()] = score
    return json.dumps(new_data)
