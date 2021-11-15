remainder = 0

def distribute(server, job):
    l1 = [] #For keeping overall list
    i = 1
    count = 0
    remainder = job%server
    for i in range (server):
        l2 = [] #For keeping the list of jobs in each server
        if job % server == 0:
            countPerServer = job/server
            if count == 0:
                for j in range (int(countPerServer)):
                    l2.append(j)
                    count = count+1
            else:
                for j in range (int(countPerServer)):
                    l2.append(j+count)
        else:
            print("remainder =", remainder)
            countPerServer = job/server
            if remainder > 0:
                if count == 0:
                    for j in range (int(countPerServer)+1):
                        l2.append(j)
                        count = count+1
                else:
                    for j in range (int(countPerServer)+1):
                        l2.append(j+count)
                        count = count+1
                remainder = remainder-1
            else:
                print("here")
                for j in range (int(countPerServer)):
                    l2.append(j+count)
                    count = count+1
        l1.append(l2)
        
    print(l1)
