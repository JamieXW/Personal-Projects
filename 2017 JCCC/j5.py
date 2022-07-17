F = open("C:\\Users\jamie\Downloads\j5\j5.09.in", "r") 
N = int(F.readline()) 
woods = (F.readline()) 

woods = woods.split(' ') 
woods[len(woods)-1] = woods[len(woods)-1].strip('\n') 

halflength = int(N/2) 

list = [] 
a = 0
b = N - 1 
for i in range (0, halflength): 
    sum = int(woods[a]) + int(woods[b]) 
    list.append(sum)
    a += 1
    b = b - 1

def most_frequent(List):
    counter = 0
    num = List[0]
      
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
  
    return num

numberofheights = most_frequent(list)

lengthofwood = list.count(most_frequent(list))
print(lengthofwood) 

##########

list2 = []
for i in range (0, halflength): 
    sum = int(woods[a]) + int(woods[b]) 
    if sum == numberofheights:
        list2.append(a)
        list2.append(b)  
    a += 1
    b = b - 1

#print(list2) 
#print(len(list2)) 