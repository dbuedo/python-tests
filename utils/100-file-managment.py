import shutil

print "File managment common operations:"

print "Open a file to Write (w): it will be created if it doen't exit; it will be overrided if it does exist"
newFile = open("new_file.txt","w")
newFile.write("write a line to a file\n")
newFile.write("end of the line is not added automagically (not cool...) \n")
newFile.write("write a second line to a file\n")
newFile.writelines([" with array ", " write ", " an ", " ordered ", " sequence ", " of ", " strings \n"])
newFile.writelines({" with a collection ", " write ", " an ", " unordered ", " sequence ", " of ", " strings "})
newFile.close()
print "Closed file"

print "Open a file to Write at the end (append) (a): file won't be overrided but modified."
newFile = open("new_file.txt","a")
newFile.write("write a line at the of the file\n")
newFile.close()
print "Closed file"

print "Open a file to Read (r): Default open() operation, so 'r' is optional."
existingFile = open("new_file.txt","r")
for line in existingFile:
    print line.rstrip()
existingFile.close()
print "Closed file"

print "Open a file to Read it directly to a data structure (small files...)."
data = open("new_file.txt").readlines()
print " line 4 : ", data[4]
print "Not close() required"


print "Copy a file low level."
fileIn = open("new_file.txt")
fileOut = open("copy.txt","w")
i = 1
for line in fileIn:
    print i, "copied line:", line.rstrip()
    fileOut.write(line)
    i = i + 1
fileIn.close()
fileOut.close()


print "For high level operations with file system, shutil and os libraries can be used "
import shutil
import os

print "Check read permission access"
if os.access("unexisting_file.txt", os.R_OK):
    print "File 'unexisting_file.txt' can be accessed in read mode"
else:
    print "File 'unexisting_file.txt' can not be accessed in read mode"

print "Create directory 'tmpDir': "
os.mkdir("tmpDir")

print "Copy a file."
shutil.copyfile("copy.txt", "tmpDir/second_copy.txt")
print "Move a file "
shutil.move("copy.txt", "tmpDir/moved.txt")

print "List content of directory 'tmpDir': "
files = os.listdir("tmpDir")
for fileName in files:
    print fileName

print "Remove files:"
for fileName in files:
    os.remove("tmpDir/" + fileName)

print "Remove directory"
os.rmdir("tmpDir")

print "Remove created files"
os.remove("new_file.txt")
    
    

    
    
    
    







