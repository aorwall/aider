LEGACY_DATA = {
    1: {"A": True, "E": True, "I": True, "O": True, "U": True, "L": True, "N": True, "R": True, "S": True, "T": True},
    2: {"D": True, "G": True},
    3: {"B": True, "C": True, "M": True, "P": True},
    4: {"F": True, "H": True, "V": True, "W": True, "Y": True},
    5: {"K": True},
    8: {"J": True, "X": True},
    10: {"Q": True, "Z": True}
}

NEW_DATA = {}
for value, letters in LEGACY_DATA.items():
    for letter in letters:
        NEW_DATA[letter.lower()] = value

def transform(legacy_data):
    if isinstance(legacy_data, int):
        return [NEW_DATA[letter.lower()] for letter in LEGACY_DATA[legacy_data]]
    elif isinstance(legacy_data, str):
        try:
            score = int(legacy_data)
            return [NEW_DATA[letter.lower()] for letter in LEGACY_DATA[score]]
        except ValueError:
            raise ValueError("Invalid input")
        except KeyError:
            raise ValueError("Invalid input")
    else:
        raise TypeError("Invalid input type")
