def binary_search(arr, value):
    """
    Performs a binary search on a sorted array to find the given value.

    Args:
        arr (list): A sorted list of values.
        value: The value to search for in the list.

    Returns:
        int: The index of the value in the list, or -1 if it is not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def find(arr, value):
    """
    Finds the index of a value in a sorted array using binary search.

    Args:
        arr (list): A sorted list of values.
        value: The value to search for in the list.

    Returns:
        int: The index of the value in the list, or -1 if it is not found.
    """
    return binary_search(arr, value)
