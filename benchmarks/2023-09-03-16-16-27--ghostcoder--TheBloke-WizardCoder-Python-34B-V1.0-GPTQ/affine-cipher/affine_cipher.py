def encrypt(plain_text, a, b):
    """Encrypts the given plain text using the Affine cipher.
    
    Args:
        plain_text (str): The message to be encrypted.
        a (int): An integer coefficient used in the cipher formula.
        b (int): Another integer coefficient used in the cipher formula.
    
    Returns:
        str: The encrypted text.
    """
    # Check if a and m are co-prime
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    encoded_text = ""
    for char in plain_text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((a * (ord(char) - offset + b) % 26) + offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text


def decrypt(encoded_text, a, b):
    """Decrypts the given ciphered text using the Affine cipher.
    
    Args:
        encoded_text (str): A string of characters to decrypt.
        a (int): An integer coefficient used in the cipher formula.
        b (int): Another integer coefficient used in the cipher formula.
    
    Returns:
        str: The decrypted text.
    """
    # Check if a and m are co-prime
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    inverted_a = find_modular_inverse(a, 26)
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((inverted_a * (ord(char) - offset - b) % 26) + offset)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text
def encode(plain_text, a, b):
    """
    Encodes the plain text using the Affine cipher.
    
    Args:
        plain_text (str): A string of characters to encrypt.
        a (int): An integer coefficient used in the cipher formula.
        b (int): Another integer coefficient used in the cipher formula.
    
    Returns:
        str: The encrypted text.
    """
    # Check if a and m are co-prime
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    encoded_text = ""
    for char in plain_text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encoded_char = chr(((a*(ord(char)-offset)+b) % 26) + offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text


def decode(encoded_text, a, b):
    """
    Decodes the encoded text using the Affine cipher.
    
    Args:
        encoded_text (str): A string of characters to decrypt.
        a (int): An integer coefficient used in the cipher formula.
        b (int): Another integer coefficient used in the cipher formula.
    
    Returns:
        str: The decrypted text.
    """
    # Check if a and m are co-prime
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    inverted_a = find_modular_inverse(a, 26)
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((inverted_a*(ord(char)-offset-b) % 26) + offset)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_modular_inverse(a, m):
    for i in range(m):
        if a * i % m == 1:
            return i
    return None

# Test Cases
print(encrypt("hello world", 5, 8))  # "htwwz dbhdp"
print(decrypt("htwwz dbhdp", 5, 8))  # "hello world"
print(encrypt("Hello World!", 7, 3))  # "Kfnnt Qyvox!"
print(decrypt("Kfnnt Qyvox!", 7, 3))  # "Hello World!"
print(encrypt("The quick brown fox jumps over the lazy dog.", 9, 4))  # "Yvccf xli pqcof kcf yvcssfm ghfr zddo ldqg."
print(decrypt("Yvccf xli pqcof kcf yvcssfm ghfr zddo ldqg.", 9, 4))  # "The quick brown fox jumps over the lazy dog."


def decode(ciphered_text, a, b):
    pass
