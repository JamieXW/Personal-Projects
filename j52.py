F = open("C:\\Users\jamie\Downloads\j5\j5\j5.01.in", "r")
rule1 = F.readline().strip()
rule1 = rule1.split(' ') 
rule2 = F.readline().strip()
rule2 = rule2.split(' ') 
rule3 = F.readline().strip()
rule3 = rule3.split(' ') 
lastline = F.readline().strip()
lastlinelist = lastline.split(' ') 
S = int(lastlinelist[0])
I = lastlinelist[1] 
F = lastlinelist[2] 

for i in range(0, S, 1): 
    if rule1[0] in I: 
        position = I.find(rule1[0]) + 1
        I = I.replace(rule1[0], rule1[1], 1)
        print("1" + " " + str(position) + " " + I) 
    elif rule2[0] in I:
        position = I.find(rule2[0]) + 1
        I = I.replace(rule2[0], rule2[1], 1)
        print("2" + " " + str(position) + " " + I)  
    elif rule3[0] in I: 
        position = I.find(rule3[0]) + 1
        I = I.replace(rule3[0], rule3[1], 1) 
        print("3" + " " + str(position) + " " + I) 