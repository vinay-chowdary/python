# Open the file mbox-short.txt and read it line by line. When you find a line that starts with
# 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.

fname = input("enter file name:")
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith("From "):
        continue
    count = count+1
    email = line.rstrip().split()[1]
    print(email)
print("There were", count, "lines in the file with From as the first word")
fhand.close()


# another way
fname = input("enter file name:")
fhand = open(fname)
count = 0
for line in fhand:
    wds = line.rstrip().split()
    if wds[0] != "From" or len(wds) == 0:
        continue
    count = count+1
    print(wds[1])
print("There were", count, "lines in the file with From as the first word")
fhand.close()
