# lists are nothing but arrays but these can hold different types of data
friends = ["a", "b", "c", "d", 0]
list2 = [1, 80, 2, 3, 10, 24, 5, 6]

# range() function gives list of values from 0 upto value specified in python2
# but in python 3 range() gives iterator.
# in python 3 we should use list() to get list from range()
print(list(range(len(friends))))

# concatenate lists
concate = friends+list2
print(concate)


# slicing lists similar to slicing strings by using : operator
print(concate[2:4])

# dir() --> lists all methods in that class(which is passed as parameter)
print(dir(list()))

# using some builtin functions on lists
concate.append([7, 8])
print(concate)
print(8 not in concate)
print(0 in concate)

# sorting list "sort() does not working if there are both int , str in list"
list2.sort()
print(list2)

# sum()
print(sum(list2))

##
lstsInLst = [[1, 2, 3], [4, 5, 6]]
for a, b, c in lstsInLst:
    print(a, b, c)
