def recite(start_verse, end_verse):
    items = ['dog', 'cat', 'rat', 'malt', 'mat', 'cockle', 'farmer sowing his corn']
    actions = ['worries', 'kisses', 'milks', 'tosses', 'ate', 'lay in']
    houses = [f"the {item} that {' '.join([action] + (['the'] if item == 'horse and hound and horn' or item == 'farmer sowing his corn' else ['a']) + [item])}" for action, item in zip(actions, items)]
    houses[-2:] = ['cocks', 'crowed'] # replace last two elements with cockle and farmer
    verses = []
    for verse in range(start_verse - 1, end_verse):
        verse_str = f"This is {houses[verse]} who {" ".join(houses[:verse][::-1])}\n"
        if verse > 0:
            verse_str = verse_str.replace("who", "that")
        verses.append(verse_str)
    return verses
