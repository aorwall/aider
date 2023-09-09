# Globals for the directions
# Change the values as you see fit
EAST = 'E'  
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH

    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH
    
    def advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == WEST:
            self.x_pos -= 1

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.turn_right()
            elif instruction == 'L':
                self.turn_left()
            elif instruction == 'A':
                self.advance()
