F = open("C:\\Users\jamie\Downloads\j2\j2\j2.sample.in", "r")
T = int(F.readline())

count = 0
while count < T: 
    N = F.readline().strip()
    list = N.split(' ')
    char = list[1]
    track = 1
    result = char
    while track < int(list[0]):
        result = result + char
        track += 1
    print(result) 
    count += 1


        
   