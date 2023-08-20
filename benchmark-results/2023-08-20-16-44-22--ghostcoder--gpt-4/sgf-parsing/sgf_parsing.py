def parse_property(input_string):
    key_end = input_string.find('[')
    if key_end == -1:
        raise ValueError("property must be in uppercase")
    key = input_string[:key_end]
    input_string = input_string[key_end:]
    values = []
    while input_string and input_string[0] == '[':
        value_end = input_string.find(']')
        if value_end == -1:
            raise ValueError("property without closing bracket")
        value = parse_value(input_string[1:value_end])
        values.append(value)
        input_string = input_string[value_end+1:]
    return key, values, input_string

def parse_value(value_string):
    result = []
    escape = False
    for char in value_string:
        if escape:
            if char != '\n':
                result.append(char)
            escape = False
        elif char == '\\':
            escape = True
        else:
            result.append(char)
    if escape:
        raise ValueError("value ends with escape character")
    return ''.join(result)