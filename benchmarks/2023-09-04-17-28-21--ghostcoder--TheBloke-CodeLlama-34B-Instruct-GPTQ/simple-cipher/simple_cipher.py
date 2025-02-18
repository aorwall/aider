import random

class Cipher:
    def __init__(self, key=None):
        self.key = key

    def _generate_key(self):
        """Generate a random key."""
        # Generate a list of 100 random lowercase letters
        key = [chr(random.randint(97, 122)) for i in range(100)]
        return ''.join(key)

    def encode(self, text):
        """Encode text using the given key."""
        # If no key was provided, generate a new one
        if not self.key:
            self.key = self._generate_key()

        # Encode each letter of the text using the corresponding letter of the key
        encoded_text = ''
        for i, char in enumerate(text):
            # Calculate the index of the character in the alphabet
            index = ord(char) - 97
            # Get the corresponding character from the key
            encoded_char = chr((index + ord(self.key[i])) % 26 + 97)
            encoded_text += encoded_char

        return encoded_text

    def decode(self, text):
        """Decode text using the given key."""
        decoded_text = ''
        for i, char in enumerate(text):
            # Calculate the index of the character in the alphabet
            index = ord(char) - 97
            # Get the corresponding character from the key
            decoded_char = chr((index - ord(self.key[i]) + 26) % 26 + 97)
            decoded_text += decoded_char

        return decoded_text

def main():
    my_message = 'Hello World!'
    print('Original message:', my_message)

    # Create a new Cipher object with a random key
    cipher = Cipher()

    # Encode the message using the key
    encoded_message = cipher.encode(my_message)
    print('Encoded message:', encoded_message)

    # Decode the message using the key
    decoded_message = cipher.decode(encoded_message)
    print('Decoded message:', decoded_message)

if __name__ == '__main__':
    main()
