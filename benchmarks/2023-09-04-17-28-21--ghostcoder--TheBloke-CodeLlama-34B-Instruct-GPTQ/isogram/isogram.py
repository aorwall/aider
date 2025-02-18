def is_isogram(string):
    """
    Determines whether a given string is an isogram or not.
    
    An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
    
    Parameters
    ----------
    string : str
        The input string to check for isogram status.
        
    Returns
    -------
    bool
        True if the input string is an isogram, False otherwise.
    """
    # Remove spaces and hyphens before checking for duplicates
    no_spaces = string.replace(' ', '').replace('-', '')
    return len(no_spaces) == len(set(no_spaces))
