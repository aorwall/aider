def square_root(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    start = 1
    end = number
    while start < end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            start = mid + 1
        else:
            end = mid

    return start
