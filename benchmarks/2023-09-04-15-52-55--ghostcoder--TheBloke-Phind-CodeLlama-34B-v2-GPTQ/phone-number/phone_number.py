import re

class PhoneNumber:
    def __init__(self, number):
        # Remove all characters except digits
        number = re.sub('[^\d]', '', str(number))

        # Check length of remaining string
        num_length = len(number)
        if num_length < 10 or num_length > 11:
            raise ValueError("Input phone number must be a 10 or 11 digit number.")

        if num_length == 11 and number[0] != '1':
            raise ValueError("If input is an 11 digit number, it must start with 1.")

        if int(number[0]) == 0:
            raise ValueError("Area Code cannot begin with 0")

        if int(number[3]) == 0:
            raise ValueError("Exchange Code cannot begin with 0")

        if int(number[0]) == 1:
            raise ValueError("Area Code cannot begin with 1")

        self.number = number

    @property
    def area_code(self):
        return self.number[:3]

    @property
    def central_office_code(self):
        return self.number[3:6]

    @property
    def line_number(self):
        return self.number[-4:]

    def pretty(self):
        return f"({self.area_code}) {self.central_office_code}-{self.line_number}"
