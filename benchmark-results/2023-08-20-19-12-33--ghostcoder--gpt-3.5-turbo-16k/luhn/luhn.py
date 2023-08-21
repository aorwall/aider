class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1:
            return False

        if not self.card_num.isdigit():
            return False

        digits = [int(digit) for digit in self.card_num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] = digits[i] * 2
            if digits[i] > 9:
                digits[i] = digits[i] - 9

        return sum(digits) % 10 == 0