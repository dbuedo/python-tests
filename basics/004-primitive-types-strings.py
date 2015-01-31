print "Strings "

print "Strings can be written like", "this", 'or like this'
print "also can be written multi-" \
	"line"
print "I " + " can " + " concatenate " + " strings " + " with " + " + " + " sign "
print "Also, I can use str(10) to concatenate other datatypes " + str(10) 
print "Can I write a new line character like in Java?\n yes, i can"
print "What about scaping \"quotes\" or \\backslashes\\? java-like-scaping :)"
print "Can I use 'simple quotes' without scaping? Yeah "
print 'Can I use "double quotes" without scaping? Cool '
print "Also, strings can be %s, as in %s " % ("formatted" , "printf")

multilineWrittenString = """This is a string which
can continue onto a new line. When printed, it will appear
   exactly as written between the trip quotes.
"""
print "multilineWrittenString " + multilineWrittenString 

print "This is very cool too: write 45 times '-': " + "-"*45

print "'string' length : ", len("string")
print "first char of 'string' : ", "string"[0]
print "last char of 'string' : ", "string"[-1]
print "substring beginning 'string' : ", "string"[:3]
print "substring inside of 'string' : ", "string"[2:4]
print "substring ending 'string' : ", "string"[3:]
print "'string' without the last char: ", "string"[:-1]

print "Comparing time!"
print "== can compare strings? : ", "THIS STRING" == "THIS STRING"
print "== can compare strings ignoring case? : ", "this STRING" == "tHiS sTring"
print "> and < can compare order of strings? : ", "THIS STRING" > "THAT STRING"
print "'in' is used like contains : ", "RING" in "STRING" 
print "'not in' is used like not contains : ", "RANG" not in "STRING" 