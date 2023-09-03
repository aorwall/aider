# Globals for the directions
# Change the values as you see fit
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, instruction):
        if instruction == 'R':
            self.rotate()
        elif instruction == 'L':
            self.rotate('left')
        else:
            self.advance()

    def rotate(self, direction='right'):
        if direction == 'right':
            if self.direction == NORTH:
                self.direction = EAST
            elif self.direction == EAST:
                self.direction = SOUTH
            elif self.direction == SOUTH:
                self.direction = WEST
            else:
                self.direction = NORTH
        else:
            if self.direction == NORTH:
                self.direction = WEST
            elif self.direction == WEST:
                self.direction = SOUTH
            elif self.direction == SOUTH:
                self.direction = EAST
            else:
                self.direction = NORTH

    def advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        else:
            self.x_pos -= 1
