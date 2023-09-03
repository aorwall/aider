import functools

def append(list1, list2):
    """Given two lists, add all items in the second list to the end of the first list."""
    return list1 + list2


def concatenate(lists):
    """Given a series of lists, combine all items in all lists into one flattened list."""
    return functools.reduce(lambda a, b: a+b, lists)

def filter(function, lst):
    """Given a predicate and a list, return the list of all items for which `predicate(item)` is True."""
    return list(filter(function, lst))

def length(lst):
    """Given a list, return the total number of items within it."""
    return len(lst)

def map(func, lst):
    """Given a function and a list, return the list of the results of applying `function(item)` on all items."""
    return list(map(func, lst))

def foldl(func, lst, acc):
    """Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left."""
    return functools.reduce(func, lst, acc)

def foldr(func, lst, acc):
    """Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right."""
    return functools.reduce(lambda x, y: func(y, x), lst[::-1], acc)

def reverse(lst):
    """Given a list, return a list with all the original items, but in reversed order."""
    return lst[::-1]


def concat(lists):
    pass


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
