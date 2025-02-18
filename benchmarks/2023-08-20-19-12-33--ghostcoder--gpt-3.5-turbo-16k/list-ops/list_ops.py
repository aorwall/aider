def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result


def filter(function, lst):
    result = []
    for item in lst:
        if function(item):
            result.append(item)
    return result


def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def map(function, lst):
    result = []
    for item in lst:
        result.append(function(item))
    return result


def foldl(function, lst, initial):
    result = initial
    for item in lst:
        result = function(result, item)
    return result


def foldr(function, lst, initial):
    result = initial
    for item in reversed(lst):
        result = function(item, result)
    return result


def reverse(lst):
    return lst[::-1]