def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = search_list[mid]

        if mid_value == value:
            return mid
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("value not in array")
