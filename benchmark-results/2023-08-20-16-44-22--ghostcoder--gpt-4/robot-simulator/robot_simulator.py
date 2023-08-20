# Globals for the directions
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'

# Define the movements for each direction
MOVEMENTS = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0)
}

# Define the turns for each direction
TURNS = {
    'R': {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH},
    'L': {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}
}


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, instructions):
        for instruction in instructions:
            if instruction in 'LR':
                self.direction = TURNS[instruction][self.direction]
            elif instruction == 'A':
                dx, dy = MOVEMENTS[self.direction]
                x, y = self.coordinates
                self.coordinates = (x + dx, y + dy)