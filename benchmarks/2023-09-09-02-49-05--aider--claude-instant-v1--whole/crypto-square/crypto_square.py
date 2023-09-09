import re

def cipher_text(plain_text):
    normalized_text = re.sub('[^a-z]', '', plain_text.lower())
    num_cols = calculate_num_cols(normalized_text)
    num_rows = calculate_num_rows(normalized_text, num_cols)
    if not normalized_text:
        return ""
    matrix = create_matrix(normalized_text, num_rows, num_cols)
    return encode_text(matrix)

def calculate_num_cols(normalized_text):
    length = len(normalized_text)
    return int(length ** 0.5) if length > 0 else 0

def calculate_num_rows(normalized_text, num_cols):
    length = len(normalized_text) 
    return length // num_cols + (1 if length % num_cols > 0 else 0)

def create_matrix(normalized_text, num_rows, num_cols):
    matrix = [""] * num_rows
    index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            try:
                matrix[row] += normalized_text[index]
            except IndexError:
                pass
            index += 1
    return matrix

def encode_text(matrix):
    encoded = ""
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            try:
                encoded += matrix[row][col] 
            except IndexError:
                pass
        if col < len(matrix[0])-1:
            encoded += " "
    return encoded.strip()
