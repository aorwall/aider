def recite(start=10, take=1):
    verses = [
        "Ten green bottles hanging on the wall, Ten green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be nine green bottles hanging on the wall.",
        "Nine green bottles hanging on the wall, Nine green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be eight green bottles hanging on the wall.",
        "Eight green bottles hanging on the wall, Eight green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be seven green bottles hanging on the wall.",
        "Seven green bottles hanging on the wall, Seven green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be six green bottles hanging on the wall.",
        "Six green bottles hanging on the wall, Six green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be five green bottles hanging on the wall.",
        "Five green bottles hanging on the wall, Five green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be four green bottles hanging on the wall.",
        "Four green bottles hanging on the wall, Four green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be three green bottles hanging on the wall.",
        "Three green bottles hanging on the wall, Three green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be two green bottles hanging on the wall.",
        "Two green bottles hanging on the wall, Two green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be one green bottle hanging on the wall.",
        "One green bottle hanging on the wall, One green bottle hanging on the wall, And if one green bottle should accidentally fall, There'll be no green bottles hanging on the wall."
    ]
    
    result = []
    for i in range(start-take, start):
        result.append(verses[i-1])
    return result
