print "Sequences "

thisIsAnEmptyArray = []
thisIsANumberArray = [ 0, 1, 2, 3 ]
thisIsAMixedTypeArray = [ 'a string', 0, 4.5, "another string"]

print "thisIsAnEmptyArray ", thisIsAnEmptyArray
print "thisIsANumberArray " , thisIsANumberArray
print "thisIsAMixedTypeArray ", thisIsAMixedTypeArray

print "thisIsAMixedTypeArray[0] ", thisIsAMixedTypeArray[0]
print "thisIsAMixedTypeArray.__len__() ", thisIsAMixedTypeArray.__len__()
print "len(thisIsAMixedTypeArray) ", len(thisIsAMixedTypeArray)

thisIsAMixedTypeArray[4:] = [9]
print "thisIsAMixedTypeArray[4:] -> ", thisIsAMixedTypeArray
thisIsAMixedTypeArray[5:] = ['added string']
print "thisIsAMixedTypeArray[5:] -> ", thisIsAMixedTypeArray
thisIsAMixedTypeArray[6:] = [" another 'added string' "]
print "thisIsAMixedTypeArray[6:] -> ", thisIsAMixedTypeArray
print "len(thisIsAMixedTypeArray) ", len(thisIsAMixedTypeArray)
thisIsAMixedTypeArray[1] = 'modified value'
print "modifies 1 position -> ", thisIsAMixedTypeArray

thisIsATuple = 1,2,3
thisIsAnotherTuple = (0, 4.5, 6L, 'string')
print "thisIsATuple ", thisIsATuple
print "thisIsAnotherTuple ", thisIsAnotherTuple
print "len(thisIsAnotherTuple) ", len(thisIsAnotherTuple)



thisIsAHashmap = { 'key1' : 'value1',
		   'key2' : 'value2',
		   'key3' : 'value3' }
thisIsAMixedTypeHashmap = { 'key1' : 'value1',
		   	    2 : 'value2',
		   	    'key3' : 3 }

print "thisIsAHashmap ", thisIsAHashmap
print "thisIsAHashmap['key2'] ", thisIsAHashmap['key2']
print "thisIsAMixedTypeHashmap ", thisIsAMixedTypeHashmap
print "thisIsAMixedTypeHashmap[2] ", thisIsAMixedTypeHashmap[2]
#print "thisIsAHashmap['key not found'] ", thisIsAHashmap['key not found'] ## -> KeyError








