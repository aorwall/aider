# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

TURN_RIGHT = ['S', 'W', 'N', 'E']
TURN_LEFT = ['E', 'N', 'W', 'S']
MOVE_FORWARD = ['E', 'N', 'W', 'S']


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, instruction):
            for cmd in instruction:
                if cmd == 'R':
                    self.direction = TURN_RIGHT[self.direction]
                elif cmd == 'L':
                    self.direction = TURN_LEFT[self.direction]
                elif cmd == 'A':
                    if self.direction == NORTH:
                        self.y_pos += 1
                    elif self.direction == SOUTH:
                        self.y_pos -= 1
                    elif self.direction == EAST:
                        self.x_pos += 1
                    else:
                        self.x_pos -= 1

            return (self.x_pos, self.y_pos)
