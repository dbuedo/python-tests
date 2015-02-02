

print "Handle exceptions is easy with try - except. Basic example: "
x = None
while x == None:
    try:
        x = int(raw_input("Please enter a number: "))
        
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

print "Well done: you entered number", x

print "Multiple exception handling and raise new Exceptions example"
x = None
while x == None:
    try:
        x = int(raw_input("Please enter a number: "))
        raise Exception("error message")
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
    except Exception as e:
        print "Exception catched : " + str(e.args)

print "Well done: you entered number", x

print "Also you can catch Unknown exceptions:"
try:
    print "this will fail because I'll try to concat an " + undeclaredVariable
except: # this way you catch every kind of exception or error possible
    print "Unknown error"



