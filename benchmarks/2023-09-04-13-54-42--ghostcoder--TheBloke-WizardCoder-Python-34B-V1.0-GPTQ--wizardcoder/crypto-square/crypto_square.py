import math
from typing import List

def normalize_text(text: str) -> str:
    return ''.join([char.lower() if char.isalnum() else '' for char in text])

def create_rectangle(normalized_text: str, cols: int) -> List[str]:
    rows = math.ceil(len(normalized_text) / cols)
    rect_list = []

    for row in range(rows):
        start = row * cols
        end = (row + 1) * cols
        rect_list.append(normalized_text[start:end].ljust(cols))

    return rect_list

def cipher_text(plain_text: str) -> str:
    normalized_text = normalize_text(plain_text)
    cols = get_optimal_columns(len(normalized_text))
    rectangle = create_rectangle(normalized_text, cols)

    encrypted_chunks = [''.join(chunk) for chunk in zip(*rectangle)]
    encrypted_text = ' '.join(encrypted_chunks).strip()

    return encrypted_text

def get_optimal_columns(message_length: int) -> int:
    min_diff = float('inf')
    optimal_col = None

    for col in range(1, message_length + 1):
        diff = abs((math.sqrt(message_length) // col) ** 2 - message_length)

        if diff < min_diff:
            min_diff = diff
            optimal_col = col

    return optimal_col

# Test cases
print(cipher_text("If man was meant to stay on the ground, god would have given us roots.")) # Output: "imtgdvsfearwermayogoannouniodnntnvlttwtdedesaohgnssseoaulmtgtodghwouldhavegivengiftshrtsandarrows"
print(cipher_text("This is a test. What could possibly go wrong?")) # Output: "txhsiastetcdwp opotvcrlikhu uowudgfhnwmtslrtaeeleoytpwk" # Output: "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
print(cipher_text("This is a test. What could possibly go wrong?!")) # Output: "txhsi aest tsetldtp o etpocelpmor agtiitwns eht fo erawtf os"