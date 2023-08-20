class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)

    def clean_number(self, number):
        # Remove all non-digit characters from the number
        cleaned_number = ''.join(filter(str.isdigit, number))

        # Remove the country code if present
        if len(cleaned_number) == 11 and cleaned_number[0] == '1':
            cleaned_number = cleaned_number[1:]

        # Check if the cleaned number is valid
        if len(cleaned_number) != 10:
            raise ValueError("Invalid phone number")

        return cleaned_number

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
