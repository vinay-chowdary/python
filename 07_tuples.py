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
