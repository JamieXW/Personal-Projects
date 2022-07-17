F = open("C:\\Users\jamie\Downloads\j4\j4.2.in", "r")
lines = int(F.readline())

allmessages = []
Rmessages = [] 

for i in range (0, lines):
    message  = F.readline() 
    message = message.split(' ') 
    message[1] = message[1].strip('\n') 
    if message[0] == 'R':
        Rmessages.append(message)
        allmessages.append(message) 
    else:    
        allmessages.append(message) 


print(allmessages)
print(Rmessages) 
 
finalarray = []
for p in range (0, len(Rmessages)):
    recieved = Rmessages[p]
    counter = 0

    for s in range (0, len(allmessages)):
        if allmessages[s][0] == 'S' and allmessages[s][1] == recieved[1]:
            if finalarray.count(recieved[1]) > 0 and finalarray.count(counter) > 0:
                counter = 0
                continue
            else:
                finalarray.append(recieved[1])
                finalarray.append(counter)
                counter = 0
                break
        elif allmessages[s][0] == 'W':
            counter += int(allmessages[s][1])

        elif allmessages[s][0] == 'R' and allmessages[s][1] == recieved[1]:
            counter = 0
        else:
            counter += 1
           

print(finalarray) 
length = len(finalarray)/2




lastarray = []
t = 0
for q in range (0, int(length)):
    output = str(finalarray[t]) + " " + str(finalarray[t+1])
    lastarray.append(output)   
    t += 2 

list = []
for r in range (0, len(lastarray)):
    (lastarray[r]) = str(lastarray[r]).split(' ')
    (lastarray[r][1]) = str(lastarray[r][1]).strip('\n')
    list.append(lastarray[r])

print(lastarray)

for z in range (0, len(list)):
    search = list[z]
    search[0] = int(search[0])
    search[1] = int(search[1]) 
    for x in range (0, len(list)):
        if search[0] == int(list[x][0]) and search[1] != int(list[x][1]):
            search[1] += int(list[x][1])
            list.remove(list[x]) 



print(list) 

#adding the values of the duplicats (23 6, 23 2)
#detecting messages that havent been replied (45) 