def answer(question):
    words = question.split()
    
    if words[0] != "What" or words[1] != "is":
        raise ValueError("invalid syntax")
        
    if len(words) == 3:
        try:
            return int(words[2][:-1])
        except ValueError:
            raise ValueError("invalid number")
        
    num1 = int(words[2][:-1])
    op = words[3]
    num2 = int(words[4][:-1])
    
    if op == "plus":
        return num1 + num2
        
    elif op == "minus":
        return num1 - num2
        
    elif op == "multiplied":
        return num1 * num2
        
    elif op == "divided":
        return num1 // num2
        
    else:
        raise ValueError("unknown operation")
