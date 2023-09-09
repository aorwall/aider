def find_fewest_coins(coins, target):
  if target < 0:
    raise ValueError("target can't be negative")
  
  if target == 0:
    return []
  
  sorted_coins = sorted(coins, reverse=True)
  
  if target < sorted_coins[-1]:
    raise ValueError(f"target {target} is smaller than smallest coin {sorted_coins[-1]}")

  selected_coins = []

  for coin in sorted_coins:
    count = target // coin
    target -= count * coin
    selected_coins.extend([coin] * count)

  if target > 0:
    raise ValueError(f"can't make target {target} with given coins")
  
  return selected_coins
