def proverb(*items):
    qualifier = ''
    if isinstance(items[-1], dict):
        qualifier = items[-1].get('qualifier', '')
        items = items[:-1]
    lines = [f'For want of a {items[i]} the {items[i+1]} was lost.' for i in range(len(items)-1)]
    lines.append(f'And all for the want of a {qualifier + " " if qualifier else ""}{items[0]}.')
    return '\n'.join(lines)
