F = open("C:\\Users\jamie\Downloads\j2\j2.2a.in", "r") 
length = int(F.readline())
votes = F.readline()

Acount = 0
Bcount = 0

k = 0
J = 1
for i in range (0, length):
    if votes[k:J] == "A":
        Acount += 1 
    else:
        Bcount += 1
    k += 1
    J += 1

print(Acount)
print(Bcount) 

if Acount > Bcount:
    print("A")
if Bcount > Acount:
    print("B")
else: 
    print("tie") 