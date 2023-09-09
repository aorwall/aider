def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target cannot be negative")
        
    if min(coins) > target:
        raise ValueError("target is smaller than smallest coin value")
        
    coins.sort(reverse=True)
    
    change = target
    result = []
    
    for coin in coins:
        if change >= coin:
            count = change // coin
            change -= count * coin
            result.append(count)
        if change == 0:
            break
            
    if change > 0:
        raise ValueError("change cannot be made with given coins")
        
    return result
