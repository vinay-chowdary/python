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
