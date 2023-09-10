class PhoneNumber:
    def __init__(self, number):
        # Check if the number is a valid phone number.
        if not self._is_valid_phone_number(number):
            raise ValueError("Invalid phone number")

        # Strip any punctuation from the number.
        self.number = number.replace("-", "").replace("(", "").replace(")", "").replace(".", "")

        # Check if the number has the correct format.
        if len(self.number) != 10 and len(self.number) != 11:
            raise ValueError("Phone number must be 10 or 11 digits")

        if len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("11-digit phone number must start with 1")

        # Split the number into its components.
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

        # Check if the exchange code and area code are valid.
        if self.exchange_code[0] == "0" or self.exchange_code[0] == "1":
            raise ValueError("Exchange code cannot start with zero or one")

        if self.area_code[0] == "0" or self.area_code[0] == "1":
            raise ValueError("Area code cannot start with zero or one")

    def _is_valid_phone_number(self, number):
        # Check if the number contains any letters or punctuation.
        for character in number:
            if character not in "0123456789":
                return False

        return True

    def pretty(self):
        # Format the phone number in a readable way.
        return "(" + self.area_code + ")-" + self.exchange_code + "-" + self.subscriber_number
