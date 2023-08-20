# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def turn_right(self):
        index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(index + 1) % len(DIRECTIONS)]

    def turn_left(self):
        index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(index - 1) % len(DIRECTIONS)]

    def advance(self):
        x, y = self.coordinates
        dx, dy = self.direction
        self.coordinates = (x + dx, y + dy)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.turn_right()
            elif instruction == 'A':
                self.advance()
            elif instruction == 'L':
                self.turn_left()
