TURN_RIGHT_DIRECTION = 1;
TURN_LEFT_DIRECTION = -1;

NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

ORIENTATIONS = [NORTH, EAST, SOUTH, WEST]

class Rover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def forward(self):
        if self.orientation == NORTH:
            self.y += 1
        elif self.orientation == SOUTH:
            self.y -= 1
        elif self.orientation == EAST:
            self.x += 1    
        elif self.orientation == WEST:
            self.x -= 1    
    
    def backward(self):
        if self.orientation == NORTH:
            self.y -= 1
        elif self.orientation == SOUTH:
            self.y += 1
        elif self.orientation == EAST:
            self.x -= 1
        elif self.orientation == WEST:
            self.x += 1

    def _turn(self, direction):
        currentOrientation = ORIENTATIONS.index(self.orientation)
        nextOrientation = (currentOrientation + direction) % len(ORIENTATIONS)
        self.orientation = ORIENTATIONS[nextOrientation]

    def left(self):       
        self._turn(TURN_LEFT_DIRECTION)
                   
    def right(self):
        self._turn(TURN_RIGHT_DIRECTION)


    def receiveCommands(self, commands):
        for command in commands:
            if command == "f":
                self.forward()
            elif command == "b":
                self.backward()  
            elif command == "l":
                self.left()
            elif command == "r":
                self.right()
    
         
                