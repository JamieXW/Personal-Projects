F = open("C:\\Users\jamie\Downloads\j4\j4.3.in", "r") 
friends = int(F.readline())
rounds = int(F.readline())

flist = [] 
k = 1
for i in range (0, friends):
    flist.append(k) 
    k += 1

print(flist) 


for i in range (0, rounds): 
    skip = int(F.readline()) 
    p = skip-1 
    for q in range (0, len(flist)):
        flist.remove(flist[p])
        p += skip-1
        if p < len(flist):
            continue
        else:
            break


print(flist) 
    
