# 1.open a file using open(filename,mode) , mode is r(read) , a(append) ,
# b(for binary file along with read or write mode), w(write) , default is read
# open returns a handler (may be a object) by use that handler to work with file
fhand = open("01_helloWorld.py")
print(fhand)

help(fhand.seek)
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
fhand = open("01_helloWorld.py")
inp = fhand.read()
print(inp)
fhand.close()
print(".................................")

# another way to open file(recommended way)
with open("01_helloWorld.py", "r") as fhand:
    linesLst = fhand.readlines()
    # similarly we can use readline() to get single line every time
    print(linesLst)


# writing into the files

# writing strings
lst = ["line1",
       "line2",
       "line3"]
with open("sample.txt", "w") as fp:
    for line in lst:
        fp.write(line+"\n")

# writing numbers the conventional way
MyNumbers = [45, 56, 90, 23, 11, 8]
with open('sample.txt', 'w') as fp:
    for num in MyNumbers:
        fp.write(str(num)+'\n')
contents = []
for num in open('sample.txt'):
    contents.append(int(num))
print(contents)

# the easier way
MyNumbers = [45, 56, 90, 23, 11, 8]
with open('mylist.txt', 'w') as fp:
    fp.write(str(MyNumbers)+'\n')
fp = open('mylist.txt')
numbers = fp.read()
print(type(numbers))
print(numbers)

MyNumbers = [45, 56, 90, 23, 11, 8]
with open('mylist.txt', 'a') as fp:
    fp.write(str(MyNumbers)+'\n')
fp = open('mylist.txt')
numbers = eval(fp.readline())
print(type(numbers))
print(numbers)
# for line in open("sample.txt"):
#     line = line.strip()
#     print(line)
