F = open("C:\\Users\jamie\Downloads\j1\j1\j1.08.in", "r")
T = F.readline()
V = F.readline()
H = F.readline() 
Q = F.readline()
W = F.readline()
E = F.readline()

Apples = int(T)*3 + int(V)*2 + int(H)
Bananas = int(Q)*3 + int(W)*2 + int(E)

if Apples > Bananas:
    print("A")
elif Bananas > Apples:
    print("B")
else:
    print("T") 




 
