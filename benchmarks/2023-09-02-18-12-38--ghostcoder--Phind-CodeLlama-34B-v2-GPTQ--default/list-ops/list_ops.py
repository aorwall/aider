def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for lst in lists:
        result += lst
    return result

def filter(function, _list):
    result = []
    for item in _list:
        if function(item):
            result.append(item)
    return result

def length(_list):
    count = 0
    for _ in _list:
        count += 1
    return count

def map(function, _list):
    result = []
    for item in _list:
        result.append(function(item))
    return result

def foldl(function, _list, initial):
    for item in _list:
        initial = function(initial, item)
    return initial

def foldr(function, _list, initial):
    for item in reversed(_list):
        initial = function(item, initial)
    return initial

def reverse(_list):
    return _list[::-1]


def filter(function, list):
    pass


def length(list):
    pass


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
