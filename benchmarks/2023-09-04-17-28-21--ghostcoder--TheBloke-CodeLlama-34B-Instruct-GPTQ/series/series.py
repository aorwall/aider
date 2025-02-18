def slices(series, length):
    """
    Returns a list of strings containing the substrings of length 'length'
    present in the input string 'series'. If there are no such substrings,
    returns an empty list.
    """
    # Initialize an empty list to store the results
    results = []

    # Check if the input series is empty
    if not series:
        raise ValueError("Series cannot be empty.")

    # Check if the slice length is valid
    if length <= 0:
        raise ValueError("Slice length must be positive.")

    # Check if the slice length is longer than the series
    if length > len(series):
        raise ValueError("Slice length cannot be greater than series length.")

    # Iterate over the series
    for i in range(len(series)):
        # Check if the current index is less than the maximum index allowed by the slice length
        if (i + length - 1) < len(series):
            # Append the substring of length 'length' starting at the current index to the results list
            results.append(series[i : i + length])

    # Return the list of substrings
    return results
