import re

class PhoneNumber:
    def __init__(self, number):
        # Remove all non-numeric characters from the string using regular expressions.
        cleaned_number = ''.join(re.findall('\d', str(number))[:10] if len(str(number)) <= 11 else '')

        # Check if the length of the cleaned number is valid.
        if len(cleaned_number) != 10:
            raise ValueError('Invalid phone number')

        self._area_code = int(cleaned_number[0:3])
        self._prefix = int(cleaned_number[3:6])
        self._line_number = int(cleaned_number[6:])

        # Validate the area code and prefix.
        if self._area_code < 2 or self._area_code > 999 or self._prefix < 2 or self._prefix > 999:
            raise ValueError('Area code must be between 2 and 999 and Exchange code must be between 2 and 999')
        elif self._area_code == 111 or self._prefix == 11:
            raise ValueError('Area code and exchange code cannot both be 11')
        else:
            self._full_number = f"({self._area_code:03d}) {self._prefix:03d} - {self._line_number:04d}"

    @property
    def full_number(self):
        return self._full_number

    @property
    def area_code(self):
        return self._area_code

    @property
    def prefix(self):
        return self._prefix

    @property
    def line_number(self):
        return self._line_number
