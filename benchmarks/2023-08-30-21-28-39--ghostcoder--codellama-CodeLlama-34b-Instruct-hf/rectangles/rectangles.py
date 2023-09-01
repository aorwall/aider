def count_rectangles(diagram):
    rectangles = 0
    for line in diagram.splitlines():
        if line.startswith("+"):
            rectangles += 1
    return rectangles

def rectangles(strings):
    pass
