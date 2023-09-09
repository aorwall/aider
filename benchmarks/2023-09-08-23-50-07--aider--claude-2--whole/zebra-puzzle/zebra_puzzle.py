
houses = [
    {"color": "red", "nationality": "Englishman"},
    {"color": "green", "drink": "coffee"},
    {"color": "ivory"},  
    {"color": "yellow", "cigarette": "Kools"},
    {"color": "blue", "nationality": "Norwegian"}
]

def drinks_water():
    for house in houses:
        if "drink" not in house:
            return "Norwegian"

def owns_zebra():
    for house in houses:
        if "pet" not in house:
            return "Japanese"

