F = open("C:\\Users\jamie\Downloads\s2_j5\s2.2.in", "r") 
question = int(F.readline())
N = int(F.readline())
speedsD = F.readline() 
speedsP = F.readline() 
speedsD = speedsD.split(' ')
speedsP = speedsP.split(' ')
speedsD[N-1] = speedsD[N-1].strip('\n')
speedsP[N-1] = speedsP[N-1].strip('\n')
print(speedsD)
print(speedsP) 
list = []
for i in range (0, N):
    list.append(speedsD[i]) 
for i in range (0, N):
    list.append(speedsP[i])

for i in range(0, len(list)):
    list[i] = int(list[i])

list.sort()
print(list) 

list2 = []
if question == 1:
    k = 0
    for i in range (0, N):
        number = max(list[k], list[k+1])
        list2.append(number)
        k += 2
elif question == 2: 
    k = 0
    q = (N + N) - 1
    for i in range (0, N):
        number = max(list[k],list[q])
        list2.append(number)
        k += 1
        q = q-1

print(list2) 

sum = 0
for i in range (0, len(list2)):
    sum = sum + list2[i]
print(sum) 