

# define a class
class Vehicle:
    # class variables are declared outside any method (equivalent to static varibles)
    legalSpeedLimit = 120;
    
    # the constructor
    def __init__(self, initSpeed=0, maxSpeed=120):
        # self is similar to this, but its use is mandatory
        self.initSpeed = initSpeed
        # instance variables are not declared outside, every 'self.varible' creates an instance variable
        self.currentSpeed = initSpeed
        # there is not visibility modifiers, everything is public
        self.maxSpeed = maxSpeed
        
    # the toString method, can not be directly invoked, is invoked when you use the str() method
    def __str__(self):
        return "Current speed " + str(self.initSpeed) + " Max speed " + str(self.maxSpeed)
    
    # self is always the first param of every function, but it is not used in the call
    def move(self):
        self.currentSpeed = self.currentSpeed + 1
        print "Moving at " + str(self.currentSpeed)
    

# Car extends Vehicle
class Car(Vehicle):
    
    numberOfWheels = 4
    
    # this method is a extension of Vehicle class, added to every Car
    def wheelsStatus(self):
        print "the car has ", self.numberOfWheels, " wheels"
        
    # this method overrides the method Vehicle.move    
    def move(self):
        self.currentSpeed = self.currentSpeed + 10
        print "Driving at " + str(self.currentSpeed)

# Motorbike is another child of Vehicle
class Motorbike(Vehicle):
    
    isHelmetOn = True
    
    def move(self):
        print "Wearing helmet?: " + str(self.isHelmetOn)
        

# multiple inheritance, MotoCar extends Motorbike and Car
# the order is important: both has a move() implementation
# in this case, Motorbike.move() prevails because it is in first place
# in this case, Motorbike.move() prevails because it is in first place
class MotoCar(Motorbike,Car):
    # finish class without adding anything
    pass

        

        
    
    


