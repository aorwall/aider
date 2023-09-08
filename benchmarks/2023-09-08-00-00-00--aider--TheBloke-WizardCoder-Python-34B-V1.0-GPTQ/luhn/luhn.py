class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.strip().replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1:
            return False

        for char in self.card_num:
            if not char.isdigit():
                return False

        total_sum = 0
        double_next = False
        for digit in self.card_num[::-1]:
            if double_next:
                doubled_digit = int(digit) * 2
                if doubled_digit > 9:
                    doubled_digit -= 9
                total_sum += doubled_digit
            else:
                total_sum += int(digit)
            double_next = not double_next

        return total_sum % 10 == 0