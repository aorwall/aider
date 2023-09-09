class PhoneNumber:
    def __init__(self, number):
        cleaned = ''.join(i for i in number if i.isnumeric())
        if len(cleaned) < 10 or len(cleaned) > 11:
            raise ValueError("Phone number must be 10 or 11 digits")
        
        if len(cleaned) == 11 and cleaned[0] != "1":
            raise ValueError("11 digit number must start with 1")

        self.number = cleaned

        area_code = self.number[:3]
        if area_code[0] == "0" or area_code[0] == "1":
            raise ValueError("Area code cannot start with 0 or 1")

        exchange_code = self.number[3:6]
        if exchange_code[0] == "0" or exchange_code[0] == "1":
            raise ValueError("Exchange code cannot start with 0 or 1")

    def pretty(self):
        return "({})-{}-{}".format(
            self.number[:3], self.number[3:6], self.number[6:]
        )
