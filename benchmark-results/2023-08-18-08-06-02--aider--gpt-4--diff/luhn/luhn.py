class Luhn:
    def __init__(self, card_num):
        self.card_num = ''.join(card_num.split())
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            self.card_num = None

    def valid(self):
        if self.card_num is None:
            return False
        digits = [int(d) for d in self.card_num]
        for i in range(-2, -len(digits) - 1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0
