remainder = 0

def distribute(server, job):
    l1 = [] #For keeping overall list
    i = 1
    count = 0
    for i in range (server):
        l2 = [] #For keeping the list of jobs in each server
        if job % server == 0:
            countPerServer = job/server
            if count == 0:
                for j in range (int(countPerServer)):
                    l2.append(j)
                    count = count+1
                    print(l2, count)
            else:
                for j in range (int(countPerServer)):
                    l2.append(j+count)
                    print(l2, count)
        else:
            remainder = job%server
            countPerServer = job/server
            if count == 0:
                for j in range (int(countPerServer)):
                    l2.append(j)
                    count = count+1
                    print(l2, count)
            else:
                for j in range (int(countPerServer)):
                    l2.append(j+count)
                    print(l2, count)
        l1.append(l2)
        
    print(l1)

distribute (2,4)
