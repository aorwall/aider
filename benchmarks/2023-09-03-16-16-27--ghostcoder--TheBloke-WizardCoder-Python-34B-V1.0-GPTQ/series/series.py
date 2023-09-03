def slices(series, length):
    """
    Returns all possible substrings of given length from the input series.
    
    Args:
        series (str): A non-empty string consisting of decimal digits.
        length (int): An integer representing the desired substring length.
    
    Returns:
        list[str]: List of all possible substrings of specified length from the input series.
    
    Raises:
        ValueError: If either series or length is empty or out of range.
    """
    # Check if series is valid
    if not series:
        raise ValueError("Series cannot be empty.")
    elif length <= 0:
        raise ValueError("Slice length cannot be zero.")
    elif length > len(series):
        raise ValueError("Slice length cannot be greater than series length.")
    else:
        return [series[i: i + length] for i in range(len(series) - length + 1)]
