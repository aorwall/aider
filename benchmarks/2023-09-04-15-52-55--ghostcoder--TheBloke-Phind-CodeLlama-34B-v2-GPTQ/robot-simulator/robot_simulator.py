from collections import defaultdict

# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3
DIRECTIONS = [EAST, NORTH, WEST, SOUTH]
TURNS = {'R': 1, 'L': -1}
STEP_SIZES = {EAST: (0, 1), NORTH: (1, 0), WEST: (0, -1), SOUTH: (-1, 0)}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, instruction):
        for turn, steps in zip(instruction[::2], map(int, instruction[1::2])):
            self.direction = (self.direction + TURNS[turn]) % 4  # Turn
            dx, dy = STEP_SIZES[DIRECTIONS[self.direction]]
            self.x_pos += dx * steps  # Move forward
            self.y_pos += dy * steps

    def get_position(self):
        return self.x_pos, self.y_pos

    def get_direction(self):
        return DIRECTIONS[self.direction]
