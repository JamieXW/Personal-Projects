F = open("C:\\Users\jamie\Downloads\j5\j5.1.in", "r")
pieces = int(F.readline())
people = int(F.readline()) 


basearray = []

for i in range (0, people):
    basearray.append(1) 

testarray =[]

print(basearray) 
counter = 0
for basearray[0] in range (1, pieces):
    for basearray[1] in range (1, pieces):
        if basearray[0] + basearray[1] == pieces:
            for i in range (0, people - 1):
                if basearray[i] < basearray[i+1] or basearray[i] == basearray[i+1]:
                    counter += 1
                    test = str(basearray[0]) + str(basearray[1]) 
                    testarray.append(test) 
                else: 
                    break
        else: 
            continue

print(counter) 
print(testarray) 