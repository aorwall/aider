def rotate(text, key):
    # Create two dictionaries, one for lowercase and one for uppercase characters
    rotation_dict_upper = {}
    rotation_dict_lower = {}

    # Fill both dictionaries with mappings from original to rotated characters
    for i in range(26):
        rotation_dict_upper[chr(i)] = chr((i - key + 26) % 26)
        rotation_dict_lower[chr(i + ord('a'))] = chr((i + key) % 26 + ord('a'))

    # Combine the two dictionaries into one
    rotation_dict = {**rotation_dict_upper, **rotation_dict_lower}

    # Rotate each character in the text using the combined dictionary
    rotated_text = ''
    for char in text:
        if char.isalpha():
            rotated_text += rotation_dict[char]
        else:
            rotated_text += char

    # Capitalize the first letter of each word if it was capitalized before encryption
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if len(word) > 0 and word[0].isupper():
            result.append(rotated_text[:len(word)-1].capitalize())
        else:
            result.append(rotated_text[:len(word)])
        rotated_text = rotated_text[len(word):]

    return ' '.join(result).replace(' ', '')
