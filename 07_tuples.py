# tuples are limited version of lists
# we cannot change tuple i.e., we cannot sort() , append() almost all oprations cannot be done on tuple
tup = (1, 2, 3, 4)

# accessing tuples are similar to lists
print(tup[2])

# looping
for iter in tup:
    print(iter)


####
lst = ((1, 2, 3), ("first", 2,
                   "all tuples must have same length to have multiple iters"), ("a", "b", "c"))
for a, b, c in lst:
    print(a, b, c)


# comparision operators will work with tuples (first compares first)
r = (1, 2, 3) == (1, 2, 2)
print(r)

# if first one is true it will not check the other values
r = (1, 2, 3) < (2, 0, 0)
print(r)

r = (1, 2, 3) > (2, 0, 0)
print(r)


# tuples and assignment
(x, y) = (1, 2)
print(x, y)


# sorting tuples
lst = [("b", 10), ("a", 20), ("word3", 2),
       ("w", 90), ("ord", 23)]
lst.sort(reverse=True)
print(lst)

# difference between class.sort() and sorted(item) is sort() rearranges the elements by modifying original list.
# where as sorted() gives an another list instead of modifying the original.


t = 10, 20, 30
t += (4,)
# t[2]=10   #cannot modify tuples

# not an inplace change


def update(t):
    t = t*2
    print(t)


update(t)
print(t)

# inplace change will not work since tuples are immutable


def updateInPlace(t):
    t *= 2
    print(t)


updateInPlace(t)
print(t)

# concatenating tuples
t1 = "1", "2"
t += t1
print(t)

t2 = t, t1
print(t2)

# slicing

print(t[2:4])
print(t[1::3])
print(t[-1::-2])

t3 = tuple("vinay")
print(t3)


tup = tuple(range(1, 15))
print(max(tup), min(tup), len(tup))
tup = tup+([100, 99, 98], ("v", "i"))
print(tup)
# tup[14] = tup[14] + [10, 20, 30] item assignment is not allowed
tup[14][2] = "added extra"
print(tup)


print(tup.count(10))
print(tup.index(14))
print(sum(tup[0:14]))
