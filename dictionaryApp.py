# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


sendersDict = dict()
fname = input("enter file name:")
fhand = open(fname)
for line in fhand:
    if not line.startswith("From "):
        continue
    email = line.rstrip().split()[1]
    sendersDict[email] = sendersDict.get(email, 0)+1
fhand.close()
maxValue = None
maxKey = None
for key, value in sendersDict.items():
    if maxValue is None or value > maxValue:
        maxValue = value
        maxKey = key
print(maxKey, maxValue)
