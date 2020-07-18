# dictionaries are similar to map or hashmap in java which are key value pairs

bag = {"one": 1, "two": 2, "three": 3}
print(bag["one"])


# starting with an empty dictionary , dict() is a constructor
bag1 = dict()
bag1["chocolates"] = 10
bag1["icecreams"] = 230
bag1["cricket-kits"] = 3
bag1["mobiles"] = 1
bag1["pc"] = 100
print(bag1)


# loop through dictionary
for key in bag1:
    print(key, bag1[key])


# converting dictionary to list of keys and list of values of dictionary
keys = list(bag1.keys())  # or simply keys=list(bag1)
values = list(bag1.values())

print(bag1.values(), values)

# finding max of values
print("max:", max(bag1.values()))


# items() gives list of tuples.each tuple is a key,value pair.
# tuples are very similar to lists.major difference is list is mutable(can be changed)
#  where as tuples are immutable(cannot be changed).list=[] , tuple=()
print(bag1.items())
# output of above line:dict_items([('chocolates', 10), ('icecreams', 230), ('cricket-kits', 3), ('mobiles', 1), ('pc', 100)])


# looping through tuples
for key, value in bag1.items():
    print(key, value)


# lets create small app to keep track of names(how may times they repeated)
tracker = dict()
while True:
    name = input("enter name: ")
    if name == "done":
        break
    if name not in tracker:
        tracker[name] = 1
    else:
        tracker[name] += 1
print(tracker)


# above app using get() in dictionaries
# if name exists already in dictionary , get returns its value ,
# else if name doesn't exist returns 0 as default
# which is provided as second parameter to get(key,default)

tracker = dict()
while True:
    name = input("enter name: ")
    if name == "done":
        break
    tracker[name] = tracker.get(name, 0)+1
print(tracker)
