import re
from typing import Optional

class PhoneNumber:
    def __init__(self, number: str):
        # Remove any non-numeric characters and leading '1'
        number = re.sub('[^0-9]', '', number)

        if len(number) == 11 and number.startswith('1'):
            area_code = number[1:4]
            prefix = number[4:7]
            line_number = number[7:]
        elif len(number) == 10:
            area_code = number[:3]
            prefix = number[3:6]
            line_number = number[6:]
        else:
            raise ValueError("Invalid phone number length.")

        self._area_code = area_code
        self._prefix = prefix
        self._line_number = line_number

    @property
    def area_code(self) -> str:
        return self._area_code

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def line_number(self) -> str:
        return self._line_number

    def pretty(self) -> str:
        return f"({self._area_code}) {self._prefix} {self._line_number}"

def main():
    try:
        number = PhoneNumber("1 (223) 456-7890")
        print(f"Area Code: {number.area_code}")
        print(f"Prefix: {number.prefix}")
        print(f"Line Number: {number.line_number}")
        print(f"Pretty Printed: {number.pretty()}\n")

        invalid_number = PhoneNumber("1234567890")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
