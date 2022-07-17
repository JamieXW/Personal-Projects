F = open("C:\\Users\jamie\Downloads\J5\J5.1-3.in", "r") 
numberofpages = int(F.readline())

list = []
for i in range (0, numberofpages):
    line = F.readline()
    inputarray = line.split(' ')
    M = 0
    for t in range (0, len(inputarray)):
        inputarray[M] = inputarray[M].strip('\n') 
        M += 1
    if int(inputarray[0]) > 0:
        k = 1
        for j in range (0, int(inputarray[0])):
            list.append(inputarray[k]) 
            k += 1
    else:
        continue  
 
count = numberofpages 
status = ""
for v in range (0, count): 
    if str(numberofpages) in list:
        status = "true"
        continue
        numberofpages = numberofpages - 1 
    else: 
        print("N")
        status = "false"
        break

if status == "true": 
    print("Y")

secondcount = count
highest = 0
for v in range (0, secondcount): 
    if str(numberofpages) in list:

      
