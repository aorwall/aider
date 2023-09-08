def append(list1, list2):
    return list1 + list2

def concatenate(lists):
    result = []
    for lst in lists:
        result += lst
    return result

def filter(predicate, lst):
    return [item for item in lst if predicate(item)]

def length(lst):
    return len(lst)

def map(function, lst):
    return [function(item) for item in lst]

def foldl(function, lst, accumulator):
    for item in lst:
        accumulator = function(accumulator, item)
    return accumulator

def foldr(function, lst, accumulator):
    for item in reversed(lst):
        accumulator = function(item, accumulator)
    return accumulator

def reverse(lst):
    return lst[::-1]
