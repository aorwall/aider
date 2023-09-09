def encode(message, rails):
    encoded = ""
    rows = create_rows(message, rails)
    for row in rows:
        encoded += "".join(row)
    return encoded

def decode(encoded_message, rails):
    rows = create_rows(encoded_message, rails) 
    for i, char in enumerate(encoded_message):
        rows[i%rails].append(char)
    message = []
    for row in rows:
        message += row
    return "".join(message)

def create_rows(text, rails):
    if text == None:
        rows = [[""] * len(encoded_message) for i in range(rails)]
    else:  
        rows = [[""] * len(text) for i in range(rails)]
        row = 0
        direction = 1
        for i, char in enumerate(text):
            rows[row][i] = char
            row += direction
            if row == rails-1 or row == 0:
                direction *= -1
    return rows
