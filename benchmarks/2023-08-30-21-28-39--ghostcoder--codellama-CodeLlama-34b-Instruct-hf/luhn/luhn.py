class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove spaces and non-digit characters from the card number
        card_num = self.card_num.replace(" ", "").replace("[^0-9]", "")

        # Check if the card number is valid
        if len(card_num) < 2:
            return False

        # Double every second digit, starting from the right
        doubled_digits = []
        for i in range(len(card_num) - 2, -1, -2):
            doubled_digits.append(int(card_num[i]) * 2)

        # Sum all the digits
        sum = 0
        for digit in doubled_digits:
            sum += digit

        # Check if the sum is evenly divisible by 10
        if sum % 10 == 0:
            return True
        else:
            return False
