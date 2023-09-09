import string

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        
    def valid(self):
        digits = []
        for char in self.card_num:
            if char in string.digits:
                digits.append(int(char))
            else:
                return False
        
        for i in range(len(digits)-2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        
        return sum(digits) % 10 == 0
