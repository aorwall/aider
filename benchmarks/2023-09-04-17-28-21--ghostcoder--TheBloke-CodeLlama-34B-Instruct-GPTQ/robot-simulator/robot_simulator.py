# Globals for the directions
# Change the values as you see fit
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        # Initialize the robot's attributes
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, instruction):
        # Implement the logic to move the robot according to the instruction
        # Use the global variables EAST, NORTH, WEST, SOUTH to determine the direction of movement
        # Update the robot's position accordingly
        # Return the final position of the robot
        if instruction == "L":
            if self.direction == NORTH:
                self.direction = WEST
            elif self.direction == WEST:
                self.direction = SOUTH
            elif self.direction == SOUTH:
                self.direction = EAST
            else:
                self.direction = NORTH
        elif instruction == "R":
            if self.direction == NORTH:
                self.direction = EAST
            elif self.direction == EAST:
                self.direction = SOUTH
            elif self.direction == SOUTH:
                self.direction = WEST
            else:
                self.direction = NORTH
        elif instruction == "M":
            if self.direction == NORTH:
                self.y_pos += 1
            elif self.direction == EAST:
                self.x_pos += 1
            elif self.direction == SOUTH:
                self.y_pos -= 1
            else:
                self.x_pos -= 1
        return [self.x_pos, self.y_pos]

def main():
    robot = Robot()
    print("Current Position: ", robot.move(""))
    print("New Position: ", robot.move("MMMRMLMM"))

if __name__ == "__main__":
    main()
