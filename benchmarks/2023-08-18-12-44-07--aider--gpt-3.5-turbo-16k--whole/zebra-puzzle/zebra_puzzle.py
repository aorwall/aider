def drinks_water():
    # Define variables for the different attributes
    houses = range(1, 6)
    colors = ['red', 'green', 'ivory', 'yellow', 'blue']
    nationalities = ['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese']
    pets = ['dog', 'snails', 'fox', 'horse', 'zebra']
    drinks = ['coffee', 'tea', 'milk', 'orange juice', 'water']
    cigarettes = ['Old Gold', 'Kools', 'Chesterfields', 'Lucky Strike', 'Parliaments']

    # Define constraints
    constraints = [
        # Constraint 2: The Englishman lives in the red house.
        ('Englishman', 'red', None),
        # Constraint 3: The Spaniard owns the dog.
        ('Spaniard', 'dog', None),
        # Constraint 4: Coffee is drunk in the green house.
        ('coffee', 'green', None),
        # Constraint 5: The Ukrainian drinks tea.
        ('Ukrainian', 'tea', None),
        # Constraint 6: The green house is immediately to the right of the ivory house.
        ('green', 'ivory', 'right'),
        # Constraint 7: The Old Gold smoker owns snails.
        ('Old Gold', 'snails', None),
        # Constraint 8: Kools are smoked in the yellow house.
        ('Kools', 'yellow', None),
        # Constraint 9: Milk is drunk in the middle house.
        ('milk', 3, None),
        # Constraint 10: The Norwegian lives in the first house.
        ('Norwegian', 1, None),
        # Constraint 11: The man who smokes Chesterfields lives in the house next to the man with the fox.
        ('Chesterfields', 'fox', 'adjacent'),
        # Constraint 12: Kools are smoked in the house next to the house where the horse is kept.
        ('Kools', 'horse', 'adjacent'),
        # Constraint 13: The Lucky Strike smoker drinks orange juice.
        ('Lucky Strike', 'orange juice', None),
        # Constraint 14: The Japanese smokes Parliaments.
        ('Japanese', 'Parliaments', None),
        # Constraint 15: The Norwegian lives next to the blue house.
        ('Norwegian', 'blue', 'adjacent')
    ]

    # Define helper functions
    def is_adjacent(house1, house2):
        return abs(house1 - house2) == 1

    def is_right(house1, house2):
        return house1 - house2 == -1

    # Define function to check if a given combination satisfies all constraints
    def satisfies_constraints(combination):
        for constraint in constraints:
            if constraint[2] == 'adjacent':
                if not is_adjacent(combination[constraint[0]], combination[constraint[1]]):
                    return False
            elif constraint[2] == 'right':
                if not is_right(combination[constraint[0]], combination[constraint[1]]):
                    return False
            else:
                if combination[constraint[0]] != constraint[1]:
                    return False
        return True

    # Generate all possible combinations of attributes
    import itertools
    combinations = list(itertools.product(houses, colors, nationalities, pets, drinks, cigarettes))

    # Check each combination to find the one that satisfies all constraints
    for combination in combinations:
        combination_dict = {
            'house': combination[0],
            'color': combination[1],
            'nationality': combination[2],
            'pet': combination[3],
            'drink': combination[4],
            'cigarette': combination[5]
        }
        if satisfies_constraints(combination_dict):
            return combination_dict['drink']

    return None


def owns_zebra():
    # Define variables for the different attributes
    houses = range(1, 6)
    colors = ['red', 'green', 'ivory', 'yellow', 'blue']
    nationalities = ['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese']
    pets = ['dog', 'snails', 'fox', 'horse', 'zebra']
    drinks = ['coffee', 'tea', 'milk', 'orange juice', 'water']
    cigarettes = ['Old Gold', 'Kools', 'Chesterfields', 'Lucky Strike', 'Parliaments']

    # Define constraints
    constraints = [
        # Constraint 2: The Englishman lives in the red house.
        ('Englishman', 'red', None),
        # Constraint 3: The Spaniard owns the dog.
        ('Spaniard', 'dog', None),
        # Constraint 4: Coffee is drunk in the green house.
        ('coffee', 'green', None),
        # Constraint 5: The Ukrainian drinks tea.
        ('Ukrainian', 'tea', None),
        # Constraint 6: The green house is immediately to the right of the ivory house.
        ('green', 'ivory', 'right'),
        # Constraint 7: The Old Gold smoker owns snails.
        ('Old Gold', 'snails', None),
        # Constraint 8: Kools are smoked in the yellow house.
        ('Kools', 'yellow', None),
        # Constraint 9: Milk is drunk in the middle house.
        ('milk', 3, None),
        # Constraint 10: The Norwegian lives in the first house.
        ('Norwegian', 1, None),
        # Constraint 11: The man who smokes Chesterfields lives in the house next to the man with the fox.
        ('Chesterfields', 'fox', 'adjacent'),
        # Constraint 12: Kools are smoked in the house next to the house where the horse is kept.
        ('Kools', 'horse', 'adjacent'),
        # Constraint 13: The Lucky Strike smoker drinks orange juice.
        ('Lucky Strike', 'orange juice', None),
        # Constraint 14: The Japanese smokes Parliaments.
        ('Japanese', 'Parliaments', None),
        # Constraint 15: The Norwegian lives next to the blue house.
        ('Norwegian', 'blue', 'adjacent')
    ]

    # Define helper functions
    def is_adjacent(house1, house2):
        return abs(house1 - house2) == 1

    def is_right(house1, house2):
        return house1 - house2 == -1

    # Define function to check if a given combination satisfies all constraints
    def satisfies_constraints(combination):
        for constraint in constraints:
            if constraint[2] == 'adjacent':
                if not is_adjacent(combination[constraint[0]], combination[constraint[1]]):
                    return False
            elif constraint[2] == 'right':
                if not is_right(combination[constraint[0]], combination[constraint[1]]):
                    return False
            else:
                if combination[constraint[0]] != constraint[1]:
                    return False
        return True

    # Generate all possible combinations of attributes
    import itertools
    combinations = list(itertools.product(houses, colors, nationalities, pets, drinks, cigarettes))

    # Check each combination to find the one that satisfies all constraints
    for combination in combinations:
        combination_dict = {
            'house': combination[0],
            'color': combination[1],
            'nationality': combination[2],
            'pet': combination[3],
            'drink': combination[4],
            'cigarette': combination[5]
        }
        if satisfies_constraints(combination_dict):
            return combination_dict['pet']

    return None
