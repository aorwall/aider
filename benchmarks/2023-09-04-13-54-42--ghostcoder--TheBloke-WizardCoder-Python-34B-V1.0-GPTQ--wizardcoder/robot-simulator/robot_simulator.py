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

    def move(self, movement):
        if movement == 'R':
            self._turn_right()
        elif movement == 'L':
            self._turn_left()
        else:
            self._advance()

    def _turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        else:
            self.direction = NORTH

    def _turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        else:
            self.direction = NORTH

    def _advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        else:
            self.x_pos -= 1

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
