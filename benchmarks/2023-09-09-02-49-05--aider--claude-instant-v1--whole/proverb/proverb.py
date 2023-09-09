def proverb(items, qualifier=None):
    lines = []
    for i in range(len(items)-1, -1, -1):
        line = f"For want of a {items[i]} the {items[i-1]}"
        if i == len(items)-1:
            line += " was lost."
        else:
            line += " was lost,"
        lines.append(line)
    if qualifier:
        lines.append(f"And {qualifier} for the want of a {items[0]}.")
    else:
        lines.append(f"And all for the want of a {items[0]}.")
    return "\n".join(lines)
