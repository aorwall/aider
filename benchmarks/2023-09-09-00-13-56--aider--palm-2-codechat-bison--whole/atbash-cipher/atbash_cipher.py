def encode(plain_text):
    """
    Encodes the given text using the Atbash cipher.

    Args:
        plain_text: The text to be encoded.

    Returns:
        The encoded text.
    """

    # Create a mapping from the letters of the alphabet to their Atbash equivalents.
    atbash_map = {
        letter: chr(ord(letter) - 26) for letter in string.lowercase
    }

    # Convert the given text to lowercase.
    plain_text = plain_text.lower()

    # Iterate over the characters in the text, replacing them with their Atbash equivalents.
    encoded_text = ""
    for character in plain_text:
        if character in atbash_map:
            encoded_text += atbash_map[character]
        else:
            encoded_text += character

    # Return the encoded text.
    return encoded_text


def decode(ciphered_text):
    """
    Decodes the given text using the Atbash cipher.

    Args:
        ciphered_text: The text to be decoded.

    Returns:
        The decoded text.
    """

    # Create a mapping from the letters of the alphabet to their Atbash equivalents.
    atbash_map = {
        letter: chr(ord(letter) + 26) for letter in string.lowercase
    }

    # Convert the given text to lowercase.
    ciphered_text = ciphered_text.lower()

    # Iterate over the characters in the text, replacing them with their Atbash equivalents.
    decoded_text = ""
    for character in ciphered_text:
        if character in atbash_map:
            decoded_text += atbash_map[character]
        else:
            decoded_text += character

    # Return the decoded