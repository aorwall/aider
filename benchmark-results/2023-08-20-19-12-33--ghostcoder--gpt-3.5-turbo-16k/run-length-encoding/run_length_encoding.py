def decode(string):
    decoded_string = ""
    count = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == "":
                count = "1"
            decoded_string += char * int(count)
            count = ""
    return decoded_string


def encode(string):
    if not string:
        return ""
    
    encoded_string = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count > 1:
                encoded_string += str(count)
            encoded_string += string[i-1]
            count = 1
    if count > 1:
        encoded_string += str(count)
    encoded_string += string[-1]
    return encoded_string