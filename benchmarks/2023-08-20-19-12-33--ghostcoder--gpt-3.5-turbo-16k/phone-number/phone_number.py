class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
        self.area_code = self.number[:3]

    def clean_number(self, number):
        cleaned_number = ""
        for char in number:
            if char.isdigit():
                cleaned_number += char
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10:
            raise ValueError("Phone number must have 10 digits")
        if cleaned_number[0] in ["0", "1"]:
            raise ValueError("Area code cannot start with zero or one")
        if cleaned_number[3] in ["0", "1"]:
            raise ValueError("Exchange code cannot start with zero or one")
        return cleaned_number

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"