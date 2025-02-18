def normalize_plaintext(plain_text):
    return plain_text.replace(" ", "").replace(",", "").replace(".", "").lower()

def dimensions(plain_text):
    n = len(normalize_plaintext(plain_text))
    r = int(math.sqrt(n)) if math.sqrt(n).is_integer() else int(math.sqrt(n)) + 1
    c = int((n / r) ** 0.5) + (1 if n % r != 0 else 0)
    return r,c

def pad_message(message, r, c):
    padded_message = message[:r*c].ljust(r*c, ' ')
    return [padded_message[i:i+c] for i in range(0, len(padded_message), c)]
def cipher_text(plain_text):
    r, c = dimensions(plain_text)
    normalized_text = normalize_plaintext(plain_text)
    matrix = pad_message(normalized_text, r, c)
    return ' '.join([''.join(row) for row in zip(*matrix)])
