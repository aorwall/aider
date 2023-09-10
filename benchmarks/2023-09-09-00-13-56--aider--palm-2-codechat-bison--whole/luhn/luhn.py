class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num) < 1:
            return False

        self.card_num = self.card_num.strip()

        for i in range(len(self.card_num) - 1, -1, -1):
            digit = int(self.card_num[i])
            digit *= 2
            if digit > 9:
                digit -= 9

        sum = 0
        for digit in self.card_num:
            sum += int(digit)

        return sum % 10 == 0
