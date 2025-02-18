def slices(series, length):
    # Check if the series is empty
    if not series:
        raise ValueError("series cannot be empty")

    # Check if the slice length is valid
    if length < 1:
        raise ValueError("slice length cannot be less than or equal to zero")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    # Generate the slices
    return [series[i:i+length] for i in range(len(series)-length+1)]
