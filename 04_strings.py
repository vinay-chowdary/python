# strings
s = "vinay"
print(len(s))
print(s[0], s[1], s[-1])
print(s[0:3], s[2:], s[:3], s[:-1])
print(s+"chowdary", s*2)


# s[0]=2 assignment error,strings are immutable
# for in-place change
l = list(s)
l[0] = "a"
s = "".join(l)
print(s)


# The bytearray supports in-place changes for text, but only for text whose characters
# are all at most 8-bits wide (e.g., ASCII).
# TODO:byte class and bytearray class
s1 = bytearray(b'spam')
s1.extend(b'eggs')
print(s1[0:2].decode())
print(s1.decode(), s.find("na"), s.replace(
    "ina", "ja"), s.upper(), s.isalpha())
print(s)
line = 'aaa,bbb,ccccc,dd\n'


# rstrip : right strip
# strips white spaces(" ",\n ..)
lst = line.rstrip().split(',')
print(lst)


######### formatting strings #########

f1 = '%s, eggs, and %s' % ('spam', 'SPAM!')
f2 = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
# numbers are optional from python 3.1+
f3 = '{}, eggs, and {}'.format('spam', 'SPAM!')
print(f1, f2, f3, sep=" == ")
print('{:,.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))


# get ascii of a letter
print(ord("@"))

# TODO: unicode strings and pattern matching pg no 106

# if the string has only digits it can be converted to integer
s = "123"
s = int(s)
s = s+1
print(s)


# implemented some of the functions


print("\n", "-"*50, end="\n\n", sep="")

str1 = "hello"
str2 = " world"

# concatenate
greet = str1+str2
print(greet)

# pulling characters out
fruit = "Banana"
print(fruit[1], fruit[4])

# len() function
print(len(fruit))

# looping through string
# basic way
index = 0
while index < len(fruit):
    print(index, fruit[index])
    index = index+1

# alternative way
for character in fruit:
    print(character)


# slicing the string by using : operator
# slice from 0th index to 3rd index,doesn't inlucde 3rd index.i.e., from 0 upto 3
print(fruit[0:3])
print(fruit[2:3])

# from starting upto 3
print(fruit[:3])

# from 3 to end here it includes last character also
print(fruit[3:])

# from start to end
print(fruit[:])

if "banana" == fruit:
    print(fruit)
elif "banana" > fruit:
    print("banana > "+fruit)
else:
    print("banana < "+fruit)


# changing case of strings
allLower = fruit.lower()
print(allLower)
allUpper = fruit.upper()
print(allUpper)

# split strings using a delimiter.default delimiter is space
splitted = greet.split()
print(splitted[1])

# find() gives the position where it was found.if not found returns -1
spacePosition = greet.find(" ")
print(spacePosition)


# search and replace
replacedGreet = greet.replace("hello world", "   hello vinay    ")
print(replacedGreet)


# stripping whitespaces lstrip() to strip left side spaces , similarly rstrip() , strip()
stripped = replacedGreet.strip()
print(stripped)


# prifixes
starts = greet.startswith("vinay")
print(starts)
