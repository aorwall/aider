class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove spaces from the card number
        card_num = self.card_num.replace(" ", "")

        # Check if the card number is valid
        if len(card_num) < 2:
            return False

        # Double every second digit, starting from the right
        doubled_digits = []
        for i in range(len(card_num) - 2, -1, -2):
            doubled_digits.append(str(int(card_num[i]) * 2))

        # Sum all the digits
        sum_digits = sum(map(int, doubled_digits))

        # Check if the sum is evenly divisible by 10
        return sum_digits % 10 == 0


def test_valid_strings_with_punctuation_included_become_invalid():
    assert Luhn("055-444-285").valid() == False

def test_valid_strings_with_symbols_included_become_invalid():
    assert Luhn("055# 444$ 285").valid() == False

def test_a_valid_canadian_sin():
    assert Luhn("055 444 285").valid() == True

def test_input_digit_9_is_correctly_converted_to_output_digit_9():
    assert Luhn("091 9").valid() == True
