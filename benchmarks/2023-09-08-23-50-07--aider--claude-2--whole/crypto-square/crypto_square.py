import re

def normalize_text(text):
    """Normalize text by removing spaces and punctuation and converting to lowercase"""
    return re.sub(r'[\s-]', '', text.lower())

def get_column_row_count(text):
    """Calculate the number of columns and rows for the cipher rectangle"""
    length = len(text)
    cols = int(length ** 0.5) # square root
    rows = cols
    if cols * rows < length:
        rows += 1
    return cols, rows

def generate_cipher_text(text):
    """Encode text using the cipher square method"""
    normalized = normalize_text(text)
    if normalized == '':
        return ''
    cols, rows = get_column_row_count(normalized)
    cipher = ""
    for c in range(cols):
        for r in range(rows):
            index = r * cols + c
            if index < len(normalized):
                cipher += normalized[index]
        if c < cols - 1:
            cipher += " "
    return cipher

def cipher_text(plain_text):
    """Main function to encode text"""
    return generate_cipher_text(plain_text)
