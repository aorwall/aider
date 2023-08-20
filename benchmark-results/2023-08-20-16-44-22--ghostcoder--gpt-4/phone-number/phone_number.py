import re

class PhoneNumber:
    def __init__(self, number):
        # Remove any non-digit characters
        cleaned = re.sub(r'\D', '', number)

        # Check the length of the cleaned number
        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned) == 11:
            if cleaned[0] != '1':
                raise ValueError("11 digits must start with 1")
            cleaned = cleaned[1:]

        # Check the area code and exchange code
        if cleaned[0] in '01':
            raise ValueError("area code cannot start with zero or one")
        if cleaned[3] in '01':
            raise ValueError("exchange code cannot start with zero or one")

        self.number = cleaned
        self.area_code = cleaned[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"