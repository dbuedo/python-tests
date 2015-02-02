from vehicle import *


print "creating vehicles..."
vehicleDefault = Vehicle()
vehicleSlow = Vehicle(0,20)

print "first : ", vehicleDefault
print "second : ", vehicleSlow

print "move vehicles..."
vehicleDefault.move()
vehicleSlow.move()    


print "Car is a child class of Vehicle"
car = Car()
car.wheelsStatus()
car.move()


print "Motorbike is another child class of Vehicle. "
moto = Motorbike()
moto.move()
