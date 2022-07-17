F = open("C:\\Users\jamie\Downloads\j3\j3.14.in", "r") 
start = F.readline()
end = F.readline()
charges = int(F.readline())

start = start.split(' ')
end = end.split(' ')
start[1] = start[1].strip('\n')
end[1] = end[1].strip('\n') 


distance = (int(end[0])-int(start[0])) + (int(end[1])-int(start[1])) 

if charges % 2 == 0:
    chargesvalue = "even"
else: 
    chargesvalue = "odd"

if distance % 2 == 0:
    distancevalue = "even"
else:
    distancevalue = "odd"
 

if distance <= charges and distancevalue == chargesvalue:
    print('Y')
else: 
    print('N')