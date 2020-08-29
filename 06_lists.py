import random
# lists are nothing but arrays but these can hold different types of data
# lists are mutable
friends = ["a", "b", "c", "d", 0]
list2 = [1, 80, 2, 3, 10, 24, 5, 6]
sample = [0]*5
print(sample)
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
print("---------------- functions ----------------")
list2.sort()
print(list2)
list2.pop(5)
print(list2)
list2.reverse()
print(list2)
print(sum(list2))
list2.insert(0, 90)
print(list2)
list2.remove(1)
print(list2)
print(list2.count(3))
print(min(list2))
print(max(list2))
print(random.choice(list2))
# print(list2.choice()) --> wrong
print(random.shuffle(list2))

# TODO:copy(),deepcopy(),sort(key=func)


lstsInLst = [[1, 2, 3], [4, 5, 6]]
for a, b, c in lstsInLst:
    print(a, b, c)


def inplaceUpdate(l):
    l += [10, 20, 30]
    print("inside  ", l)


def noInPlaceUpdate(l):
    l = l+[40, 50]
    print("inside  ", l)


lst = [1, 2, 3]
inplaceUpdate(lst)
print("outside ", lst)

noInPlaceUpdate(lst)
print("outside ", lst)


print(lst[::-1])
print(lst[5:2:-1])
