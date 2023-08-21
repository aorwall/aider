class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove spaces from the card number
        card_num = self.card_num.replace(" ", "")

        # Check if the card number is valid
        if len(card_num) <= 1:
            return False

        # Check if the card number contains only digits
        if not card_num.isdigit():
            return False

        # Double every second digit, starting from the right
        digits = [int(digit) for digit in card_num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

        # Sum all the digits
        total = sum(digits)

        # Check if the sum is divisible by 10
        if total % 10 == 0:
            return True
        else:
            return False
