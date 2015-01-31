


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


# while statement
fact = 1
i = 1
while i <= value and i <= 15:
   fact = fact * i
   print i, "! = ", fact
   i = i + 1

print "TOTAL: ", fact

# for statement
print "counting to 10 from 0"
for i in xrange(10):
    print i

print "counting to 10 from 1"
for i in xrange(1, 11):
    print i

print "counting from 5 to 15"
for i in xrange(5, 16):
    print i

print "counting to 10 by 2 "
for i in xrange(0, 11, 2):
    print i

print "counting letters in a string!!. ej: "
chars = 0
vowels = 0
for ch in "CHIRIPITIFLAUTICO":
    chars = chars + 1
    if(ch in "AEIOU"):
        vowels = vowels + 1
print "CHIRIPITIFLAUTICO has", chars, "characters,", vowels, "are vowels."









