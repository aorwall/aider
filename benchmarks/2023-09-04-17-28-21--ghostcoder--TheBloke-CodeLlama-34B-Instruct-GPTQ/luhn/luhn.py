import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove spaces from the card number
        card_num = self.card_num.replace(' ', '')

        # Check if the card number is valid
        if len(card_num) <= 1 or not card_num.isdigit():
            return False

        # Double every second digit starting from the right
        total = 0
        for i in range(-1, -len(card_num), -2):
            digit = int(card_num[i])
            if digit >= 5:
                digit -= 9
            total += digit

        # Sum all the digits
        total += sum(map(int, card_num[-1::-2]))

        # If the total is divisible by 10, the card number is valid
        return total % 10 == 0
