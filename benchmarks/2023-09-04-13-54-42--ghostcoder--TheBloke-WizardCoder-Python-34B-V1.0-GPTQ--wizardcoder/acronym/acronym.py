import re

def abbreviate(phrase):
    words = re.findall(r"[a-zA-Z']+", phrase)
    acronym = "".join([word[0].upper() for word in words if not word[-1]=="'"])
    return acronym

# Test cases
print(abbreviate("As Soon As Possible")) # ASAP
print(abbreviate("Liquid-crystal display")) # LCD
print(abbreviate("Thank George It's Friday!")) # TGIF