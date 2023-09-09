def primes(limit):
    numbers = list(range(2, limit+1))
    
    for i in numbers:
        if i == 0 or i == 1:
            continue
            
        for j in numbers[i*2::i]:
            if numbers[j-i] != 0:
                numbers[j-i] = 0
            
    return [n for n in numbers if n!=0]
