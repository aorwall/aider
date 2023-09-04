def drinks_water():
    # Create a dictionary for each statement related to the house location
    house_location = {'Englishman': 1, 'Spaniard': 2, 'Ukrainian': 3, 'Norwegian': 5}

    # Create a dictionary for statements related to the profession, pet, drink, and cigarette brand
    profession_pet_drink_cigarette = {'Chesterfields': 2, 'Fox': 2, 'Kools': 3, 'Horse': 3, 'LuckyStrike': 4, 'OrangeJuice': 4, 'Parliaments': 4, 'Japanese': 5}

    # Check the conditions
    for key, value in profession_pet_drink_cigarette.items():
        if value == house_location['Norwegian'] - 1:
            return key


def owns_zebra():
    # Create a dictionary for each statement related to the house location
    house_location = {'Englishman': 1, 'Spaniard': 2, 'Ukrainian': 3, 'Norwegian': 5}

    # Create a dictionary for statements related to the profession, pet, drink, and cigarette brand
    profession_pet_drink_cigarette = {'Chesterfields': 2, 'Fox': 2, 'Kools': 3, 'Horse': 3, 'LuckyStrike': 4, 'OrangeJuice': 4, 'Parliaments': 4, 'Japanese': 5}

    # Check the conditions
    for key, value in profession_pet_drink_cigarette.items():
        if value == house_location[key] + 1:
            return key
