F = open("C:\\Users\jamie\Downloads\j1\j1.samp1.in", "r") 

outcomes = F.readlines() 


k = 0
for i in range (0, 6):
    outcomes[k] = outcomes[k].strip('\n') 
    k += 1


counter = 0
m = 0
for i in range (0, 6):
    if outcomes[m] == "W":
        counter += 1
        m += 1
    else: 
        m += 1
        

if int(counter) == 5 or int(counter) == 6:
    print("1") 
elif int(counter) == 3 or int(counter) == 4:
    print("2")
elif int(counter) == 1 or int(counter) == 2:
    print("3")
else: 
    print("-1") 
