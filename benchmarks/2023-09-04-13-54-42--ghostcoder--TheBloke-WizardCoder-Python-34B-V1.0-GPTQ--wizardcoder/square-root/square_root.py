import math

def square_root(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Radicand must be a non-negative integer")

    # Use binary search algorithm to find square root
    low, high = 0, number
    while low <= high:
        mid = (low + high) // 2

        if pow(mid, 2) == number:
            return mid

        elif pow(mid, 2) > number:
            high = mid - 1

        else:
            low = mid + 1

    return round((low + high) / 2)
