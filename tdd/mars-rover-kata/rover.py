
class Rover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def forward(self):
        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'E':
            self.x += 1    
        elif self.orientation == 'W':
            self.x -= 1    
    
    def backward(self):
        if self.orientation == 'N':
            self.y -= 1
        elif self.orientation == 'S':
            self.y += 1
        elif self.orientation == 'E':
            self.x -= 1
        elif self.orientation == 'W':
            self.x += 1
    
    def left(self):
        if self.orientation == 'N':
            self.orientation = 'W'
        elif self.orientation == 'S':
            self.orientation = 'E'
        elif self.orientation == 'E':
            self.orientation = 'N'
        elif self.orientation == 'W':
            self.orientation = 'S'
                   
    def right(self):
        if self.orientation == 'N':
            self.orientation = 'E'
        elif self.orientation == 'S':
            self.orientation = 'W' 
        elif self.orientation == 'E':
            self.orientation = 'S' 
        elif self.orientation == 'W':
            self.orientation = 'N' 

    def move(self, commands):
        for command in commands:
            if command == "f":
                self.forward()
            elif command == "b":
                self.backward()  
            elif command == "l":
                self.left()
            elif command == "r":
                self.right()
    
         
                