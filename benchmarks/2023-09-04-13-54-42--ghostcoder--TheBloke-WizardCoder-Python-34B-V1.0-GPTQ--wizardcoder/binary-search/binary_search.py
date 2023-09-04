def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

class BinarySearch():
    def __init__(self, search_list):
        self.search_list = search_list

    def find(self, value):
        """
        Implement binary search here. Return index of value in search_list, or -1 if not present.
        
        :param value: int
        :return: int
        """
        result = binary_search(self.search_list, value)
        if result != -1:
            return result
        else:
            raise ValueError("value not in array")