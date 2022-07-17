F = open("C:\\Users\jamie\Downloads\j2\j2.samp1.in", "r") 
row1 = F.readline()
row2 = F.readline()
row3 = F.readline()
row4 = F.readline()

row1 = row1.split(' ') 
row2 = row2.split(' ') 
row3 = row3.split(' ') 
row4 = row4.split(' ') 

row1[3] = row1[3].strip('\n') 
row2[3] = row2[3].strip('\n') 
row3[3] = row3[3].strip('\n') 
row4[3] = row4[3].strip('\n') 

a = int(row1[0]) + int(row1[1]) + int(row1[2]) + int(row1[3])
b = int(row2[0]) + int(row2[1]) + int(row2[2]) + int(row2[3])
c = int(row3[0]) + int(row3[1]) + int(row3[2]) + int(row3[3])
d = int(row4[0]) + int(row4[1]) + int(row4[2]) + int(row4[3])
e = int(row1[0]) + int(row2[0]) + int(row3[0]) + int(row4[0])
f = int(row1[1]) + int(row2[1]) + int(row3[1]) + int(row4[1])
g = int(row1[2]) + int(row2[2]) + int(row3[2]) + int(row4[2])
h = int(row1[3]) + int(row2[3]) + int(row3[3]) + int(row4[3]) 


if a == b and b == c and c == d and d == e and e == f and f == g and g == h:
    print("magic")
else: print("not magic") 