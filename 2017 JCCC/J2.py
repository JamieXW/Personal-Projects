F = open("C:\\Users\jamie\Downloads\j2\j2.15.in", "r") 
x = int(F.readline())
n = int(F.readline())

counter = x
startnumber = x
for i in range (0, n):
    startnumber = startnumber * 10
    counter = counter + startnumber

print(counter) 