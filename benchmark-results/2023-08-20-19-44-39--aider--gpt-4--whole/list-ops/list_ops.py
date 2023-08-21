def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for sublist in lists for item in sublist]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum(1 for _ in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reversed(list):
        result = function(result, item)
    return result


def reverse(list):
    return list[::-1]
