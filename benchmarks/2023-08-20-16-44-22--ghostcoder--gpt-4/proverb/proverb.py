def proverb(items, qualifier=None):
    qualifier = '' if qualifier is None else qualifier
    lines = [f'For want of a {x} the {y} was lost.' for x, y in zip(items, items[1:])]
    lines.append(f'And all for the want of a {qualifier + " " if qualifier else ""}{items[0]}.')
    return '\n'.join(lines)