def find(search_list, value):
    """Perform a binary search to find the index of the first occurrence of the value in the search_list.
    
    Args:
        search_list (list): A sorted list of integers.
        value (int): An integer to search for in the search_list.
    
    Returns:
        int: Index of the first occurrence of the value in the search_list.
            Raises a ValueError if the value is not found in the list.
    """
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == value:
            # Check if this is the first occurrence of the value
            if mid == 0 or search_list[mid - 1] != value:
                return mid
            else:
                high = mid - 1
        elif search_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError("value not in array")
