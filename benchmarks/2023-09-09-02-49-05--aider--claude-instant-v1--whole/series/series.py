def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")
        
    if length < 1:
        raise ValueError("slice length cannot be negative or zero")
        
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
        
    slices = []
    for i in range(len(series)-length+1):
        slices.append(series[i:i+length])
    return slices
