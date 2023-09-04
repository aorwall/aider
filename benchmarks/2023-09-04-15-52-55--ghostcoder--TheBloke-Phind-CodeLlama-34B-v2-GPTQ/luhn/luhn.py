import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = re.sub("\D", "", card_num)   # Remove non-digits

    def valid(self):
        nums = list(map(int, self.card_num))
        reverse_nums = nums[::-1]

        total = 0
        index = 0
        while len(reverse_nums) > 0:
            num = reverse_nums.pop()

            if (index % 2 != 0): # Double every second digit
                num *= 2

                if (num >= 10): # If doubling the number results in a number greater than 9 then subtract 9 from the product
                    num -= 9

            total += num
            index += 1

        return total % 10 == 0 # The sum is evenly divisible by 10, then the number is valid
