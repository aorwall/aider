def proverb(inputs, qualifier=None):
    if not inputs:
        return []

    def build_sentence(noun1, noun2):
        return f"For want of a {noun1} the {noun2} was lost."

    sentences = [build_sentence(inputs[i], inputs[i + 1]) for i in range(len(inputs) - 1)]
    sentences.append(f"And all for the want of a {inputs[0]}.")

    if qualifier:
        sentences[-1] = f"And all for the want of a {qualifier}."

    return sentences
