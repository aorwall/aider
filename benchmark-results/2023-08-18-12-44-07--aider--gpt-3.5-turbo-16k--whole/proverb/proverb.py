def proverb(inputs, qualifier=None):
    if len(inputs) == 0:
        return ""

    lines = []
    for i in range(len(inputs) - 1):
        lines.append(f"For want of a {inputs[i]} the {inputs[i+1]} was lost.")

    if qualifier:
        lines.append(f"And all for the want of a {qualifier}.")
    else:
        lines.append(f"And all for the want of a {inputs[0]}.")

    return "\n".join(lines)
