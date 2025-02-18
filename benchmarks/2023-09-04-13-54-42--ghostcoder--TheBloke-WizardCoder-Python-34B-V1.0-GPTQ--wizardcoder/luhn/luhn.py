import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.strip()

    def _double_second_digits(self, num):
        new_num = ""
        for i, char in enumerate(reversed(num)):
            if (i + 1) % 2 == 0:
                try:
                    doubled = int(char) * 2
                    if doubled > 9:
                        doubled -= 9
                    new_num += str(doubled)
                except ValueError:
                    continue
            else:
                new_num += char

        return new_num[::-1]

    def _sum_digits(self, num):
        total = 0
        for char in num:
            total += int(char)

        return total

    def valid(self):
        cleaned_num = re.sub('[^0-9 ]', '', self.card_num)
        if len(cleaned_num) <= 1:
            return False

        doubled_num = self._double_second_digits(cleaned_num)
        total = self._sum_digits(doubled_num)

        return total % 10 == 0
