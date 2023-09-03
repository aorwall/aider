def slices(series, length):
    # Check for exceptions
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    elif length <= 0:
        raise ValueError("slice length cannot be zero or negative")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[i: i + length] for i in range(len(series) - length + 1)]
