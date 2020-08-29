# max number of jobs can be done

def endVal(j):
    return j[1]


total = int(input("number of activities"))
lst = list()
for i in range(total):
    start = int(input("start"))
    end = int(input("end"))
    job = (start, end)
    lst.append(job)


lst.sort(key=endVal)
print("sorted on end time ", lst)
prevJobEnd = lst[0][1]
jobsCanBeDone = 1
for job in lst[1:]:
    if(job[0] <= prevJobEnd):
        jobsCanBeDone += 1
        prevJobEnd = job[1]

print("total jobs can be done", jobsCanBeDone)
