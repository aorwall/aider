import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = re.sub(r"\D", "", card_num)

    def valid(self):
        sum = 0
        card_num = self.card_num[::-1]

        for i, digit in enumerate(card_num):
            digit = int(digit)
            if i % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum += digit

        return sum % 10 == 0
