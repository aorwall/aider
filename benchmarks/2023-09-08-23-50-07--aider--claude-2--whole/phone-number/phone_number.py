import re

class PhoneNumber:
    def __init__(self, number):
        number = re.sub(r"[^\d]", "", number)
        if len(number) < 10:
            raise ValueError("Number must be at least 10 digits")
        if len(number) > 11:
            raise ValueError("Number must be no more than 11 digits")
        if len(number) == 11 and number[0] != "1":
            raise ValueError("11 digit number must start with 1")
        
        if len(number) == 10:
            number = "1" + number
        
        area_code = number[:3]
        exchange_code = number[3:6]
        subscriber_number = number[6:]
        
        if area_code[0] == "0":
            raise ValueError("Area code cannot start with 0")
        
        if exchange_code[0] == "0" or exchange_code[0] == "1":
            raise ValueError("Exchange code cannot start with 0 or 1")
        
        self.number = number

