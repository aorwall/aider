import re
class PhoneNumber:
    def __init__(self, number):
        # Remove all characters except digits
        cleaned = re.sub('[^\d]', '', str(number))

        # Check length before and after cleaning
        if len(cleaned) < 10 or len(cleaned) > 11:
            raise ValueError("must have 10 or 11 digits")

        # If 11 digits, it must start with a 1
        elif len(cleaned) == 11 and cleaned[0] != '1':
            raise ValueError("11 digits must start with 1")

        # Clean up based on different lengths
        if len(cleaned) == 11:
            self.areacode = cleaned[1:4]
            self.exchange = cleaned[5:8]
            self.subscriber = cleaned[9:]
        else:
            self.areacode = cleaned[:3]
            self.exchange = cleaned[3:6]
            self.subscriber = cleaned[6:]

        # Validate area code and exchange code
        for code in [self.areacode, self.exchange]:
            if code[0] in ['0', '1']:
                raise ValueError("codes cannot start with zero or one")

        # Set the final phone number
        self.number = f"{self.areacode}{self.exchange}{self.subscriber}"

    def pretty(self):
        return f"({self.areacode})-{self.exchange}-{self.subscriber}"
