def transpose(lines):
    # Split each line into a list of words
    lines = [line.split() for line in lines]

    # Find the longest list of words
    max_words = max(len(line) for line in lines if len(line) > 0)

    # Transpose the lists of words
    transposed = []
    for i in range(max_words):
        transposed.append([])
        for line in lines:
            try:
                word = line[i]
            except IndexError:
                word = ""
            transposed[-1].append(word)

    # Join each list of words into a single string
    transposed = [" ".join(line) for line in transposed]

    return "\n".join(transposed)
