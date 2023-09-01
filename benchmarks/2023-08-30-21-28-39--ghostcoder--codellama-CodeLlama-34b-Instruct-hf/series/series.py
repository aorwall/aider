def slices(series, length):
    """
    Returns a list of all contiguous substrings of length `length` in the input string.
    
    :param series: The input string.
    :param length: The length of the substrings to return.
    :return: A list of substrings.
    """
    if not series or length < 1:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    result = []
    for i in range(len(series) - length + 1):
        result.append(series[i:i+length])
    return result
