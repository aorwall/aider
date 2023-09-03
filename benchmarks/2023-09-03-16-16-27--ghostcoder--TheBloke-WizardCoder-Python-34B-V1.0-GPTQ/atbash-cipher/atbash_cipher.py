def encode(plain_text):
    """Encode plain text using the Atbash cipher"""
    # Create a dictionary mapping each letter to its corresponding cipher text character.
    atbash_dict = {chr(97+i): chr(97+(26-i) % 26) if i < 14 else chr(97+(26-(i - 13)) % 26) for i in range(26)}

    # Remove non-letter characters and split into chunks of 5 characters (or less)
    cleaned_text = ''.join([char for char in plain_text if char.isalpha()]).lower()
    chunked_text = [cleaned_text[i:i+5] for i in range(0, len(cleaned_text), 5)]

    # Encode each chunk by replacing each letter with its mapped value in the atbash_dict
    encoded_chunks = [''.join([atbash_dict[char] for char in chunk]) for chunk in chunked_text]

    # Join the chunks back together and separate them with spaces every 5 characters
    joined_encoded = ' '.join([''.join(chunk) for chunk in encoded_chunks])

    return joined_encoded


def decode(ciphered_text):
    """Decode ciphered text using the Atbash cipher"""
    # Invert the atbash_dict to create a decoding dictionary
    decoding_dict = {value:key for key, value in atbash_dict.items()}

    # Split the ciphered text into chunks of 5 characters (or less)
    chunked_text = [ciphered_text[i:i+5].strip().lower() for i in range(0, len(ciphered_text), 5)]

    # Decode each chunk by replacing each letter with its mapped value in the decoding_dict
    decoded_chunks = [''.join([decoding_dict[char] for char in chunk]) for chunk in chunked_text]

    # Join the chunks back together without spaces
    joined_decoded = ''.join([''.join(chunk) for chunk in decoded_chunks])

    return joined_decoded
