def find(search_list, value):
    left_idx = 0
    right_idx = len(search_list) - 1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_val = search_list[mid_idx]
        
        if mid_val == value:
            return mid_idx
        elif mid_val < value:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
            
    raise ValueError("value not in array")
