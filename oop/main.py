from vehicle import *


print "creating vehicles..."
vehicleDefault = Vehicle()
vehicleSlow = Vehicle(0,20)

print "first : ", vehicleDefault
print "second : ", vehicleSlow

print "move vehicles..."
vehicleDefault.move()
vehicleSlow.move()    
