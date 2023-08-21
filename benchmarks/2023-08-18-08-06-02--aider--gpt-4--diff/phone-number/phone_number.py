import re

class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)

    def clean_number(self, number):
        cleaned = re.sub(r'\D', '', number)

        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned) == 11 and cleaned[0] != '1':
            raise ValueError("11 digits must start with 1")
        elif len(cleaned) == 11 and (cleaned[1] == '0' or cleaned[1] == '1'):
            raise ValueError("area code cannot start with zero or one")
        elif len(cleaned) == 10 and (cleaned[0] == '0' or cleaned[0] == '1'):
            raise ValueError("area code cannot start with zero or one")
        elif cleaned[3] == '0' or cleaned[3] == '1':
            raise ValueError("exchange code cannot start with zero or one")

        return cleaned[1:] if len(cleaned) == 11 else cleaned

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def area_code(self):
        return self._number[:3]

    def pretty(self):
        return f"({self._number[:3]})-{self._number[3:6]}-{self._number[6:]}"
