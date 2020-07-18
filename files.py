# 1.open a file using open(filename,mode) , mode is r(read) or w(write) , default is read
# open returns a handler (may be a object) by use that handler to work with file
fhand = open("helloWorld.py")
print(fhand)


# reading files
# for loop is smart enough to read a line from file handler
# line has a \n at last and print() also adds \n so we get empty lines between lines.
# to deal with those empty lines we strip off the \n character from the line.(since \n is a white space we can use rstrip())
for line in fhand:
    line = line.rstrip()
    if not line.startswith("#"):
        print(line)
fhand.close()
# reading whole file using read()
print(".................................")
fhand = open("helloWorld.py")
inp = fhand.read()
print(inp)
fhand.close()
print(".................................")
