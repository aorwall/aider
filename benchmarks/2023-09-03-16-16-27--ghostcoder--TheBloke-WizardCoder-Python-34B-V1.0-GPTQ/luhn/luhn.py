class Luhn:
    def __init__(self, card_num):
        self.card_num = ''.join([c for c in str(card_num) if c.isdigit()]) # remove spaces and non-numeric characters

    def valid(self):
        if len(self.card_num) <= 1:
            return False
        total = 0
        for i, num in enumerate(reversed(self.card_num)):
            if (i % 2 == 1):
                doubled = int(num) * 2
                if doubled > 9:
                    doubled -= 9
            else:
                doubled = int(num)
            total += doubled
        return total % 10 == 0
