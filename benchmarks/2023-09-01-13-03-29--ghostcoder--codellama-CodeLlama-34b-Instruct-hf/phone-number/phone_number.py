import re
class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
        if not self.is_valid():
            raise ValueError("Invalid phone number")

    def clean_number(self, number):
        """
        Remove punctuation and country code from a phone number.
        
        Args:
            number (str): The phone number to clean.
        
        Returns:
            str: The cleaned phone number.
        """
        # Remove punctuation
        number = re.sub(r'[^\d]', '', number)

        # Remove country code
        if number.startswith('1'):
            number = number[1:]

        return number

    def is_valid(self):
        """
        Check if the phone number is valid.
        
        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        # Check if the number has 10 digits
        if len(self.number) != 10:
            return False

        # Check if the area code is valid
        if self.number[0] == '0' or self.number[0] == '1':
            return False

        # Check if the exchange code is valid
        if self.number[3] == '0' or self.number[3] == '1':
            return False

        return True

    def __str__(self):
        return self.number
