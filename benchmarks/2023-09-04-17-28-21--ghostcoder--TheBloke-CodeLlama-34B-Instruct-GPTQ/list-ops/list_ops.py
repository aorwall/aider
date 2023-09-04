def append(list1, list2):
    return list1 + list2


def concat(lists):
    return sum(lists, [])


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    acc = initial
    for element in list:
        acc = function(acc, element)
    return acc


def foldr(function, list, initial):
    acc = initial
    for element in reversed(list):
        acc = function(element, acc)
    return acc


def reverse(list):
    return list[::-1]
