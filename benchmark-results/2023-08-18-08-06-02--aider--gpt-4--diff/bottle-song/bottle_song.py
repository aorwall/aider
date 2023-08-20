def number_to_words(n):
    if n == 0:
        return 'no more'
    words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    return words[n]

def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        bottle = 'bottle' if i == 1 else 'bottles'
        next_bottle = 'no more bottles' if i == 1 else f'{number_to_words(i-1)} bottles'
        verse = f"{number_to_words(i).capitalize()} green {bottle} hanging on the wall,\n" \
                 f"{number_to_words(i).capitalize()} green {bottle} hanging on the wall,\n" \
                 "And if one green bottle should accidentally fall,\n" \
                 f"There'll be {next_bottle} hanging on the wall.\n"
        verses.append(verse)
    return '\n'.join(verses)
