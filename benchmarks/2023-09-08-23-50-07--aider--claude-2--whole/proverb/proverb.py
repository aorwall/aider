def proverb(items, qualifier=None):
    items = items[::-1]
    text = []
    for i in range(len(items) - 1):
        text.append(f"For want of a {items[i]} the {items[i+1]} was lost.") 
    if qualifier:
        text.append(f"And all for the want of a {items[0]} {qualifier}.")
    else:
        text.append(f"And all for the want of a {items[0]}.")
    return "\n".join(text)
