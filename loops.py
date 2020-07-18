
# don't print line if it starts with # , if done is typed end the loop
while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)

# for loop
for i in [1, 2, 3, 4, 5]:
    print(i)

friends = ["a", "b", "c"]
for friend in friends:
    print("Hello", friend)

# find largest of all
# The None keyword is used to define a null value, or no value at all.
# None is not the same as 0, False, or an empty string. None is a datatype of its own (NoneType) and only None can be None.
largest = None
for i in [27, 22, 1, 90, 54, 9, 10]:
    if largest is None or largest < i:
        largest = i
print("largest", largest)

# "is" operator in python is similar to "===" in javascript. It considers both type and value
