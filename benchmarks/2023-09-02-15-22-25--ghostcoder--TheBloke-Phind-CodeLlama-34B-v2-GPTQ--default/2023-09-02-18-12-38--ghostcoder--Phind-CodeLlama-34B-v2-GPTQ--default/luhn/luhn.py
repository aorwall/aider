class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        sum = 0
        for i in range(len(self.card_num)):
            digit = int(self.card_num[i])

            if (len(self.card_num) - i) % 2 == 0:
                digit *= 2

                if digit > 9:
                    digit -= 9

            sum += digit

        return sum % 10 == 0
