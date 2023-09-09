def maximum_value(maximum_weight, items):

    items.sort(key=lambda x: x['value']/x['weight'], reverse=True)
    
    total_value = 0
    total_weight = 0
    
    for item in items:
        if total_weight + item['weight'] <= maximum_weight:
            total_value += item['value'] 
            total_weight += item['weight']
        else:
            fractional_item_weight = maximum_weight - total_weight
            fractional_item_value = item['value'] * fractional_item_weight / item['weight']
            total_value += fractional_item_value
            total_weight = maximum_weight
            break
            
    return total_value
