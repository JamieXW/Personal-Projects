F = open("C:\\Users\jamie\Downloads\j5\j5\j5.11.in", "r") 
M = int(F.readline()); N = int(F.readline()); length = int(F.readline()) 

list = []

for i in range (0, length, 1):
    item = str(F.readline())
    list.append(item) 

list = sorted(list, key=str.lower)
#print(list) 

new = []
k = 0
while k < length - 1:
    if list[k] == list[k+1]:
        k += 2 
        continue
    else:
        new.append(list[k])
        k += 1

if list[length-2] != list[length-1]:
    new.append(list[length-1])


#print(new) 

b = 0
numberofcs = 0
numberofrs = 0
for i in range (0, len(new), 1):
    if str(new[b][:1]) == "C":
        numberofcs += 1
        b += 1
    elif str(new[b][:1]) == "R":
        numberofrs += 1
        b += 1

total = (numberofcs * int(M)) + (numberofrs * int(N)) - (numberofcs * numberofrs * 2) 
print(total) 