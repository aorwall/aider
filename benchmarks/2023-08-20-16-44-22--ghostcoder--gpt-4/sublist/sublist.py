SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif any(list_one == list_two[i:i+len(list_one)] for i in range(len(list_two))):
        return SUBLIST
    elif any(list_two == list_one[i:i+len(list_two)] for i in range(len(list_one))):
        return SUPERLIST
    else:
        return UNEQUAL