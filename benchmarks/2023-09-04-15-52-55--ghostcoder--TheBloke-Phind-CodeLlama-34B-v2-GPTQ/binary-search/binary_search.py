def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = search_list[mid]

        if guess == value:
            return mid
        elif guess > value:
            high = mid - 1
        else:
            low = mid + 1

    # Value was not found in the list, raise an error
    raise ValueError('value not in array')
