def maximum_value(maximum_weight, items):
  # Sort items by value/weight ratio
  items.sort(key=lambda x: x["value"] / x["weight"], reverse=True)
  
  total_value = 0
  current_weight = 0
  
  for item in items:
    if current_weight + item["weight"] <= maximum_weight:
      # Take entire item
      total_value += item["value"]
      current_weight += item["weight"]
    else:
      # Item too heavy, skip it
      continue
      
  return total_value
