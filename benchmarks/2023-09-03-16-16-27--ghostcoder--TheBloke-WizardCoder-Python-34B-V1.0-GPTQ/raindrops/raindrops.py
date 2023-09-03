def convert(number):
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    divisible_by = {num: sounds[num] for num in [3, 5, 7] if number % num == 0}

    if not divisible_by:
        return str(number)
    else:
        return ''.join([sounds[divisible] for divisible in sorted(divisible_by)]).replace('Plink', '').replace('Plank', '')
