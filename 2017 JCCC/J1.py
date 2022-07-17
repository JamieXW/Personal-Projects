F = open("C:\\Users\jamie\Downloads\j1\j1.15.in", "r") 
x = int(F.readline())
y = int(F.readline()) 

print(x,y) 

quadrant = 1

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
else: 
    quadrant = 4

print(quadrant) 
