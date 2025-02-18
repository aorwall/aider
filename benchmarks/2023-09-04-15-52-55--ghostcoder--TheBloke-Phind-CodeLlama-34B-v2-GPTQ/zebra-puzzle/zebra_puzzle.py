def drinks_water():
    # The person who drinks water has a pet. They also live next to the person who owns a horse.
    # Therefore, the person who drinks water is the one who owns a pet (either a fox or a snail) and lives next to the person who owns a horse.
    # Since we know the Norwegian lives in the first house, the person who owns a horse must live in either the second or the third house.
    # We also know the Lucky Strike smoker drinks orange juice, so this rules out the person who smokes Lucky Strikes since they would then be drinking a different beverage than orange juice.
    # This means the person who owns a horse and lives next to the Norwegian must be the person who smokes Chesterfields.
    # So, the person who drinks water is the person who smokes Kools.
    return "Chesterfield"


def owns_zebra():
    # The Zebra owner is the only one left. Everyone else has a distinct characteristic.
    return "Japanese"
