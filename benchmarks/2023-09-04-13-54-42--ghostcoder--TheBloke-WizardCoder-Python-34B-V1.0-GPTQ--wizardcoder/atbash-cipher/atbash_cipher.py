def encode(plain_text):
    plain_text = plain_text.lower()

    # Create a dictionary to store the mapping between plain and cipher characters
    char_mapping = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')

    # Replace each character in the plain text with its corresponding cipher character using the mapping
    cipher_text = plain_text.translate(char_mapping)

    # Group the cipher text into chunks of 5 characters separated by spaces
    grouped_chars = [cipher_text[i:i+5].upper() for i in range(0, len(cipher_text), 5)]

    final_cipher_text = ' '.join(grouped_chars)

    return final_cipher_text


def decode(ciphered_text):
    # Invert the character mapping to get the decryption mapping
    char_mapping = str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')

    # Remove spaces and convert the cipher text to lower case
    ciphered_text = ciphered_text.lower().replace(' ', '')

    # Apply the decryption mapping to each character in the cipher text
    plain_text = ciphered_text.translate(char_mapping)

    return plain_text
