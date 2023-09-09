# Globals for the directions
EAST = 'E'  
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

class Robot:
    def __init__(self, x_pos=0, y_pos=0, direction=NORTH):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction
        
    def turn_right(self):
        # turn right logic
        
    def turn_left(self):
       # turn left logic 
           
    def move_forward(self):
       # advance logic
           
    def move(self, instructions):
        for char in instructions:
            if char == 'R':
                self.turn_right()
            elif char == 'L': 
                self.turn_left()
            else:
                self.move_forward()
                
   @property
   def coordinates(self):
       return (self.x_pos, self.y_pos)
