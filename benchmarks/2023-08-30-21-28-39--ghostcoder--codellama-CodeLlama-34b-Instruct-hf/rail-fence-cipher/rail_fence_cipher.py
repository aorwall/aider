def encode(message, rails):
    # Initialize an empty list to store the encoded message
    encoded_message = []

    # Iterate over the rails
    for i in range(rails):
        # Add the message characters to the encoded message list
        # If the message length is less than the number of rails,
        # the remaining characters will be filled with spaces
        encoded_message.extend(message[i::rails])

    # Join the encoded message list into a single string
    return "".join(encoded_message)


def decode(encoded_message, rails):
    # Initialize an empty list to store the decoded message
    decoded_message = []

    # Iterate over the rails
    for i in range(rails):
        # Add the encoded message characters to the decoded message list
        # If the encoded message length is less than the number of rails,
        # the remaining characters will be filled with spaces
        decoded_message.extend(encoded_message[i::rails])

    # Join the decoded message list into a single string
    return "".join(decoded_message)
