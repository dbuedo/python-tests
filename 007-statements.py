


# if statement

value = int(raw_input( "Enter an integer:"))

if value < 0 :
   print "The value is negative."
   value = abs( value )
else:
   print "The value is positive."
   
# there is now switch, if-elif-else instead

if value >= 90.0 :
   letterGrade = "A"
elif value >= 80.0 :
   letterGrade = "B"
elif value >= 70.0 :
   letterGrade = "C"
elif value >= 60.0 :
   letterGrade = "D"
else:
   letterGrade = "F"   
   
print "Value " + str(value) + " is a grade " + letterGrade

