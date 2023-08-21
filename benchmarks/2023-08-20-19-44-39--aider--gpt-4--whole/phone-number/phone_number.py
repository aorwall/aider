import re

class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
        self.area_code = self.number[:3]

    def clean_number(self, number):
        # Remove all non-digit characters
        cleaned = re.sub(r'\D', '', number)

        # Check for valid number length
        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned) == 11:
            if cleaned[0] != '1':
                raise ValueError("11 digits must start with 1")
            cleaned = cleaned[1:]

        # Check for valid area code and exchange code
        if cleaned[0] in '01':
            raise ValueError("area code cannot start with zero or one")
        if cleaned[3] in '01':
            raise ValueError("exchange code cannot start with zero or one")

        return cleaned

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
