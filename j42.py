F = open("C:\\Users\jamie\Downloads\j4\s1_j4\j4.sample02.in", "r")
N = F.readline()


length = int(len(N)) - 1
topleft = 1
topright = 2
bottomleft = 3
bottomright = 4
c = str(N[0])

for i in range(0, length, 1):
    c = str(N[i]) 
    if c == "V":
        temp = topleft
        topleft = topright
        topright = temp
        temp2 = bottomleft
        bottomleft = bottomright
        bottomright = temp2
    elif c == "H":
        temp = topleft
        topleft = bottomleft
        bottomleft = temp
        temp2 = topright
        topright = bottomright
        bottomright = temp2 

print(topleft, topright)
print(bottomleft, bottomright) 

    
