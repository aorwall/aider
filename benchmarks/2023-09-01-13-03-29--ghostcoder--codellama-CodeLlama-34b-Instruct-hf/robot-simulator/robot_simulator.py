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

    def move(self, direction):
        if direction == "L":
            self.direction = (self.direction - 1) % 4
        elif direction == "R":
            self.direction = (self.direction + 1) % 4
        else:
            raise ValueError("Invalid direction")

    def coordinates(self):
        return (self.x_pos, self.y_pos)


def test_robot():
    robot = Robot(NORTH, 3, 8)
    assert robot.coordinates() == (3, 8)
    assert robot.direction == NORTH

    robot.move("L")
    assert robot.coordinates() == (3, 8)
    assert robot.direction == WEST

    robot.move("R")
    assert robot.coordinates() == (3, 8)
    assert robot.direction == NORTH

    robot.move("L")
    assert robot.coordinates() == (3, 8)
    assert robot.direction == SOUTH

    robot.move("R")
    assert robot.coordinates() == (3, 8)
    assert robot.direction == EAST


if __name__ == "__main__":
    test_robot()
