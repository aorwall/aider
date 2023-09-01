# Globals for the directions
# Change the values as you see fit
EAST = None
NORTH = None
WEST = None
SOUTH = None


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos, y_pos)

    def move(self, direction):
        if direction == "L":
            self.direction = (self.direction - 1) % 4
        elif direction == "R":
            self.direction = (self.direction + 1) % 4
        elif direction == "F":
            if self.direction == NORTH:
                self.y_pos += 1
            elif self.direction == EAST:
                self.x_pos += 1
            elif self.direction == SOUTH:
                self.y_pos -= 1
            else:
                self.x_pos -= 1
        self.coordinates = (self.x_pos, self.y_pos)


def test_robot_movement():
    robot = Robot(NORTH, 7, 3)
    robot.simulate(["RAALAL"])
    assert robot.x_pos == 9
    assert robot.y_pos == 4
    assert robot.direction == WEST


if __name__ == "__main__":
    test_robot_movement()
