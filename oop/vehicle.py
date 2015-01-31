
# define a class
class Vehicle:
    # the constructor
    def __init__(self, initSpeed=0, maxSpeed=120):
        # self is similar to this, but its use is mandatory
        self.initSpeed = initSpeed
        # instance variables are not declared outside, every 'self.varible' creates an instance variable
        self.currentSpeed = initSpeed
        self.maxSpeed = maxSpeed
        
    # the toString method, can not be directly invoked, is invoked when you use the str() method
    def __str__(self):
        return "Current speed " + str(self.initSpeed) + " Max speed " + str(self.maxSpeed)
    
    # self is always the first param of every function, but it is not used in the call
    def move(self):
        self.currentSpeed = self.currentSpeed + 1
        print "Moving at " + str(self.currentSpeed)
    


