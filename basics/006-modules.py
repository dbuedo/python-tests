
# import a function (or all) from a module

from math import *


print "MATH MODULE"

x = float(raw_input( "Enter a real value:"))
y = sqrt(x)
print "The square root of", x, "is", y

print "round(y) - Computes and returns the y rounded: ", round(y)
print "ceil(y) - Computes and returns the ceiling of y: ", ceil(y)
print "floor(y) - Computes and returns the floor of y: ", floor(y)
print "sqrt(y) - Computes the square root of y: ", sqrt(y)
print "degrees(y) - Converts the radians x to degrees: ", degrees(y)
print "radians(y) - Converts the angle x from degrees to radians: ", radians(y)


# imports can be done anywhere, always before any use of that module
print "DATETIME MODULE"

from datetime import *

oneDate = date(2015,01,15)
today = date.today()
whichDay = today.weekday()
now = datetime.now()
nowFormatted = datetime.strftime(now, "%d/%m/%y %H:%M")
nowFormattedAnotherWay = now.strftime("%d-%m-%y_%H-%M")


print "oneDate ", oneDate
print "today ", today
print "whichDay ", whichDay
print "now ", now
print "nowFormatted ", nowFormatted
print "nowFormattedAnotherWay ", nowFormattedAnotherWay

