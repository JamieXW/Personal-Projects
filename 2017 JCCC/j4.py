F = open("C:\\Users\jamie\Downloads\j4\j4.15.in", "r") 
minutes = int(F.readline()) 

time = [1, 2, 0, 0]


counter = 0
for i in range (0, minutes):
    time[3] = time[3] + 1
    if time[3] > 9:
        time[2] = time[2] + 1
        time[3] = 0
    if time[2] > 5: 
        time[1] += 1
        time[2] = 0
    if time[0] == 1 and time[1] > 2: 
        time[0] = 0
        time[1] = 1
    if time[1] > 9 and time[0] == 0:
        time[0] += 1
        time[1] = 0
    a = time[1] - time[0]
    b = time[2] - time[1]
    c = time[3] - time[2] 
    if a == b == c and time[0] == 1: 
        counter += 1 
    if b == c and time[0] == 0:
        counter += 1

print(time) 
print(counter) 