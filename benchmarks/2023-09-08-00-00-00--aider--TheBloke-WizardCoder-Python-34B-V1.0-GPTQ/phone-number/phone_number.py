class PhoneNumber:
    def __init__(self, number):
        import re

        # Remove any punctuation and convert to a string
        number = re.sub(r'[^\w\s]', '', str(number))

        # Remove any letters
        number = re.sub(r'[a-zA-Z]', '', number)

        # Remove the country code if present
        if number.startswith('1'):
            number = number[1:]

        # Check if the number has exactly 10 digits
        if len(number) != 10:
            raise ValueError("must be exactly 10 digits")

        # Check if the area code starts with 0 or 1
        if number[0] in ['0', '1']:
            raise ValueError("area code cannot start with zero or one")

        # Check if the exchange code starts with 0 or 1
        if number[3] in ['0', '1']:
            raise ValueError("exchange code cannot start with zero or one")

        self.number = number

    def __str__(self):
        return self.number

    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
