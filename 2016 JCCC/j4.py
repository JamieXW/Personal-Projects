F = open("C:\\Users\jamie\Downloads\j4\j4.samp3.in", "r") 
time = F.readline() 
time = time.split(':')
time[1] = time[1].strip('\n') 
print(time)
time[0] = int(time[0])
time[1] = int(time[1]) 
if time[1] == 60: 
    time[0] += 1
    time[1] = 00
if time[0] == 24:
    time[0] = 00

counter = 0
for i in range (0, 120):
    if time[0] == 7 or time[0] == 8 or time[0] == 9:
        if time[1] == 60: 
            time[0] += 1
            time[1] = 00
        if time[0] == 24:
            time[0] = 00
        time[1] += 2
        counter += 1
        continue
    elif time[0] == 15 or time[0] == 16 or time[0] == 17 or time[0] == 18:
        if time[1] == 60: 
            time[0] += 1
            time[1] = 00
        if time[0] == 24:
            time[0] = 00
        time[1] += 2
        counter += 1
        continue
    else:
        if time[1] == 60: 
            time[0] += 1
            time[1] = 00
        if time[0] == 24:
            time[0] = 00
        time[1] += 1
        continue

if time[1] == 60: 
    time[0] += 1
    time[1] = 00
if time[0] == 24:
    time[0] = 00
print(time) 

    



