F = open("C:\\Users\jamie\Downloads\j2\j2\j2.sample.02.in", "r")
participents = int(F.readline())

highestbidder = ["blank",0] 
for i in range (0, participents, 1):
    array = []
    Name = F.readline()
    array.append(Name) 
    bid = int(F.readline())
    array.append(bid) 
    if array[1] > highestbidder[1]:
        highestbidder = array
print(highestbidder[0]) 

