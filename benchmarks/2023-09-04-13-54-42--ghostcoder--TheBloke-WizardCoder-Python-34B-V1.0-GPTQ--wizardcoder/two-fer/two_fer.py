def two_fer(name="you"):
    if not name:
        name = "you"

    message = f"One for {name}, one for me."
    return message