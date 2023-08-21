# Globals for the directions
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def turn_right(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def turn_left(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

    def advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y + 1)
        elif self.direction == EAST:
            self.coordinates = (x + 1, y)
        elif self.direction == SOUTH:
            self.coordinates = (x, y - 1)
        else:  # self.direction == WEST
            self.coordinates = (x - 1, y)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.turn_right()
            elif instruction == 'A':
                self.advance()
            elif instruction == 'L':
                self.turn_left()
