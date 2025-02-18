from typing import Callable, List

def append(list1: List, list2: List) -> List:
    return list1 + list2


def concat(lists: List[List]) -> List:
    result = []
    for lst in lists:
        result += lst
    return result


def filter(function: Callable[[object], bool], lst: List) -> List:
    return [x for x in lst if function(x)]


def length(lst: List) -> int:
    return len(lst)


def map(function: Callable[[object], object], lst: List) -> List:
    return [function(x) for x in lst]


def foldl(function: Callable[[object, object], object], lst: List, initial: object) -> object:
    acc = initial
    for x in lst:
        acc = function(acc, x)
    return acc


def foldr(function: Callable[[object, object], object], lst: List, initial: object) -> object:
    acc = initial
    for x in reversed(lst):
        acc = function(x, acc)
    return acc


def reverse(lst: List) -> List:
    return lst[::-1]