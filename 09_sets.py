# TODO:pagenumber:123
s = {}  # this creates a empty dictionary
print(type(s))

# to create set
s1 = set("vinaychowdary")
s2 = set("VinayChowdary")
print(s1, s2)
print(s1 | s2)  # union
print(s1-s2)  # difference
print(s1 & s2)  # intersection
print(s1 ^ s2)  # x-y U y-x
print(s1 > s2)  # superset
print(s1 < s2)  # subset
print(s1.intersection(s2))
print(s1.union(s2))


print("\n", "-"*50, "functions", "-"*50, "\n")


s3 = "17282"
s1.add("ch")
print(s1)
s1.update(s3)
print(s1)
s1.remove("c")
print(s1)
s1.discard("i")
print(s1)
print(s1.issubset(s2))
print(s1.issuperset(s2))
# copy(),clear(),del,symmetric_difference()
