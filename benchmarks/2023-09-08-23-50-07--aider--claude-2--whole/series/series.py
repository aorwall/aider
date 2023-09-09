def slices(series, length):
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length <= 0:
        if length == 0:
            raise ValueError("slice length cannot be zero")
        else:
            raise ValueError("slice length cannot be negative")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    output = []
    for i in range(len(series) - length + 1):
        output.append(series[i:i+length])
    return output
