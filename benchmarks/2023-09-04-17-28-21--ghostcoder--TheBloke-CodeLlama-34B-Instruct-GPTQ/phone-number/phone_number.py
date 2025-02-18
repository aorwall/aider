import re

class PhoneNumber:
    def __init__(self, number):
        self._number = None
        pattern = r"\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*"
        match = re.match(pattern, str(number))
        if match:
            groups = match.groups()
            self._number = f"({groups[0]})-{groups[1]}-{groups[2]}"
        else:
            raise ValueError("Invalid phone number.")

    @property
    def pretty(self):
        return self._number

def main():
    print(PhoneNumber("+1 (613)-995-0253").pretty) # +1 613-995-0253
    print(PhoneNumber("613-995-0253").pretty) # +1 613-995-0253
    print(PhoneNumber("1 613 995 0253").pretty) # +1 613-995-0253
    print(PhoneNumber("613.995.0253").pretty) # +1 613-995-0253

if __name__ == '__main__':
    main()
