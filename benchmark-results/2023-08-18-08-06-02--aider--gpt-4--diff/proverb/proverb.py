def proverb(items, qualifier=None):
    if not items:
        return ''
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    lines.append(f"And all for the want of a {qualifier + ' ' if qualifier else ''}{items[0]}.")
    return '\n'.join(lines)
