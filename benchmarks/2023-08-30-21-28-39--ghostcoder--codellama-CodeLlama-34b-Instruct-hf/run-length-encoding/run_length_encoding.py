def encode(string):
    encoded_string = ""
    count = 1
    for i in range(len(string)):
        if i > 0 and string[i] != string[i-1]:
            encoded_string += str(count) + string[i-1]
            count = 1
        else:
            count += 1
    encoded_string += str(count) + string[i]
    return encoded_string

def decode(string):
    decoded_string = ""
    i = 0
    while i < len(string):
        if string[i].isdigit():
            count = int(string[i])
            decoded_string += count * string[i+1]
            i += 2
        else:
            decoded_string += string[i]
            i += 1
    return decoded_string
