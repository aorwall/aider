def find(search_list, value):
    start = 0
    end = len(search_list) - 1

    while start <= end:
        middle = (start + end) // 2
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            end = middle - 1
        else:
            start = middle + 1

    raise ValueError("value not in array")