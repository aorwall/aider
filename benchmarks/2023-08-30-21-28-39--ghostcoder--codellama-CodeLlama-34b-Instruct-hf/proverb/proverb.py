def proverb(qualifier):
    result = []
    for i in range(len(qualifier)):
        result.append(f"For want of a {qualifier[i]} the {qualifier[i+1]} was lost.")
    result.append(f"And all for the want of a {qualifier[0]}.")
    return "\n".join(result)


def proverb():
    pass
