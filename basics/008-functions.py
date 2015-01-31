
def basicFunction(param1, param2):
    print "param1 is " + str(param1) + " and param2 is " + str(param2)
    return str(param1) + str(param2)

print "basicFuncntion with param1 = a and param2 = b returns : " + basicFunction("a", "b")

print "params are polymorphic : param1 = 1 and param2 = b returns : " + basicFunction(1, "b")

print "params are polymorphic : param1 = True and param2 = 10.2 returns : " + basicFunction(True, 10.2)

def functionWithDefaults(param1 = False, param2 = False, param3 = False):
    if param1:
        print "    param1 is passed True"
    if param2: 
        print "    param2 is passed True"
    if param3:
        print "    param3 is passed True"
        
print "function can have default values for params. So you can call a fucntion"
print "this way: "
functionWithDefaults(True, True, True)
print "or this way:"
functionWithDefaults(True, True)
print "or this other way:"
functionWithDefaults(True)
print "or even without params:"
functionWithDefaults()

print "functions always returns something, if there isn't return statements it will return : " , functionWithDefaults()

print "Another cool feature is passing functions to another fucntions by parameters."
def move(animal="Humans", kindOfMove="watch TV"):
    return animal + " " + kindOfMove + "."
def run():
    return "run"
def fly():
    return "fly"
def swim():
    return "swim"
print move("Lions",run())
print move("Birds",fly())
print move("Fishes",swim())
print move()






