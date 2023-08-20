def encode(message, rails):
    if rails == 1:
        return message
    
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in message:
        fence[rail].append(char)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
    
    encoded_message = ''
    for rail in fence:
        encoded_message += ''.join(rail)
    
    return encoded_message


def decode(encoded_message, rails):
    if rails == 1:
        return encoded_message
    
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in encoded_message:
        fence[rail].append(None)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
    
    index = 0
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = encoded_message[index]
            index += 1
            
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
    
    decoded_message = ''
    rail = 0
    direction = 1
    
    for _ in range(len(encoded_message)):
        decoded_message += fence[rail].pop(0)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
            
        rail += direction
    
    return decoded_message
