def encode(message, rails):
    # Initialize the encoded message to an empty string
    encoded_message = ""

    # Loop through each rail
    for i in range(rails):
        # Add the message characters at the current rail position to the encoded message
        for j in range(i, len(message), rails):
            encoded_message += message[j]

    return encoded_message


def decode(encoded_message, rails):
    # Initialize the decoded message to an empty string
    decoded_message = ""

    # Loop through each rail
    for i in range(rails):
        # Add the encoded message characters at the current rail position to the decoded message
        for j in range(i, len(encoded_message), rails):
            decoded_message += encoded_message[j]

    return decoded_message
