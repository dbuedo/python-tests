TURN_RIGHT_DIRECTION = 1
TURN_LEFT_DIRECTION = -1
FORWARD_DIRECTION = 1
BACKWARD_DIRECTION = -1

NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

ORIENTATIONS = [NORTH, EAST, SOUTH, WEST]
MOVE_STEP = {
             NORTH : ( 0,  1),
             EAST  : ( 1,  0),
             SOUTH : ( 0, -1),
             WEST  : (-1,  0)
             }

class Rover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation


    def _move(self, direction):
        step = MOVE_STEP[self.orientation]
        self.x += step[0] * direction
        self.y += step[1] * direction

    def forward(self):
        self._move(FORWARD_DIRECTION)
    
    def backward(self):
        self._move(BACKWARD_DIRECTION)

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
    
         
                