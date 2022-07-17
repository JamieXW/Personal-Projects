F = open("C:\\Users\jamie\Downloads\j3\j3\j3.06.in", "r")
Q = F.readlines()
k = 0
for i in range (0,len(Q), 1):
    Q[k] = Q[k].strip('\n')
    k += 1

summ = int(Q[0][:1]) + int(Q[0][1:2])
if summ % 2 == 0:
    pathdirection = "right"
    print(pathdirection + " " + str(Q[0][2:5]))
else:
    pathdirection = "left" 
    print(pathdirection + " " + str(Q[0][2:5]))

count = 1
for i in range (0,int(len(Q)) -2, 1):
    direction1 = int(Q[count][:1])
    direction2 = int(Q[count][1:2])
    sum = direction1 + direction2
    if sum % 2 == 0:
        pathdirection = "right"
        print(pathdirection + " " + str(Q[count][2:5])) 
        count += 1
    elif sum == 0:
        print(pathdirection + " " + str(Q[count][2:5])) 
        count += 1
    else:
        pathdirection = "left"
        print(pathdirection + " " + str(Q[count][2:5]))
        count += 1 