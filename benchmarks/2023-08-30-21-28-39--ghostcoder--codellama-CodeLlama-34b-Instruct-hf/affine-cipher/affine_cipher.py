def encode(plain_text, a, b):
    """
    Encodes the plain text using the affine cipher.
    
    Parameters:
        plain_text (str): The plain text to encode.
        a (int): The first parameter of the affine cipher.
        b (int): The second parameter of the affine cipher.
    
    Returns:
        str: The encoded text.
    """
    # Check if a and m are coprime
    if a < 1 or a > 26 or b < 1 or b > 26 or math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    # Encrypt the text
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            index = ord(char) - ord("A")
            cipher_text += chr((a * index + b) % 26 + ord("A"))
        else:
            cipher_text += char

    # Return the encrypted text
    return cipher_text


def decode(cipher_text, a, b):
    """
    Decodes the cipher text using the affine cipher.
    
    Parameters:
        cipher_text (str): The cipher text to decode.
        a (int): The first parameter of the affine cipher.
        b (int): The second parameter of the affine cipher.
    
    Returns:
        str: The decoded text.
    """
    # Check if a and m are coprime
    if a < 1 or a > 26 or b < 1 or b > 26 or math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    # Decrypt the text
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            index = ord(char) - ord("A")
            plain_text += chr((math.modinv(a, 26) * (index - b)) % 26 + ord("A"))
        else:
            plain_text += char

    # Return the decrypted text
    return plain_text


def decode(ciphered_text, a, b):
    pass
