class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)

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
        if len(self.number) != 10:
            raise ValueError("Phone number must be 10 digits long")

        if self.number.startswith('0'):
            raise ValueError("Phone number cannot start with 0")

        if self.number.startswith('1'):
            raise ValueError("Phone number cannot start with 1")

        return True

    def __str__(self):
        return self.number
