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
    print(recieved) 
    for s in range (0, len(allmessages)):
        if allmessages[s][0] == 'S' and allmessages[s][1] == recieved[1]:
            finalarray.append(recieved[1])
            finalarray.append(counter)
            counter = 0
            print(counter)
            break
        elif allmessages[s][0] == 'W':
            counter += int(allmessages[s][1])
            print(counter)
        elif allmessages[s][0] == 'R' and allmessages[s][1] == recieved[1]:
            counter = 0
        else:
            counter += 1
            print(counter) 

print(finalarray) 
length = len(finalarray)/2

lastarray = []
t = 0
for q in range (0, int(length)):
    output = str(finalarray[t]) + " " + str(finalarray[t+1])
    lastarray.append(output)   
    t += 2 

print(lastarray) 

#1. code cannot detect duplication of recieved messages, therefore mimics and last output for the respective person (23 6, 23 6) 
#2. the rules are messed up, lines arent being counted right
#3. code cannot detect messages that havent been replied
#4. 