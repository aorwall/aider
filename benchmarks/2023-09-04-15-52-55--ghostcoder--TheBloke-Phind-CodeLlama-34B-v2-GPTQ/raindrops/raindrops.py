def convert(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    results = []
    for factor, sound in factors.items():
        if number % factor == 0:
            results.append(sound)

    if len(results) == 0:
        results.append(str(number))

    return ''.join(results)
