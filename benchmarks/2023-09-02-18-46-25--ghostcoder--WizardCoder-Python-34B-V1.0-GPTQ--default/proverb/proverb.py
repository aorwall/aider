def proverb(lst, *, qualifier="all"):
    def_str = "For want of a {} the {} was lost."
    last_line = f"And all for the want of {qualifier}." if qualifier else "And all for the want of a nail."
    result = []
    for i in range(len(lst) - 1):
        result.append(def_str.format(lst[i], lst[i+1]))
    result.append(last_line)
    return "\n".join(result)