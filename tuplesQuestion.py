# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line  by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
timeDict = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 6 or words[0] != "From":
        continue
    time = words[5].split(":")[0]
    timeDict[time] = timeDict.get(time, 0)+1
for k, v in sorted(timeDict.items()):
    print(k, v)
