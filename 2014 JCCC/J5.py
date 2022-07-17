F = open("C:\\Users\jamie\Downloads\j5\j5.2a.in", "r") 
students = int(F.readline())
list1 = F.readline() 
list2 = F.readline() 

list1 = list1.split(' ') 
list1[len(list1)-1] = list1[len(list1)-1].strip('\n') 

list2 = list2.split(' ') 
list2[len(list2)-1] = list2[len(list2)-1].strip('\n') 

print(list1)
print(list2) 

finallist = [] 
for i in range (0, students): 
    item = []
    item.append(list1[i])
    item.append(list2[i])
    item = sorted(item)
    finallist.append(item) 

print(finallist)
secondlist = finallist 
mark = "good" 
for i in range (0, len(secondlist)): 
    for w in range (0, len(finallist)):
        count = finallist.count(secondlist[i]) 
        if count == 2:
            continue
        else:
            mark = "bad"
            break

print(mark) 


