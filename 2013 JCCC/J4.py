F = open("C:\\Users\jamie\Downloads\J4\j4.5.in", "r") 
time = int(F.readline())
chores = int(F.readline()) 

list = []
for i in range (0, chores):
    amount = int(F.readline())
    list.append(amount)

list.sort() 
print(list) 


counter = 0
for i in range (0, len(list)):
    time = time - list[i] 
    if time >= 0: 
        counter += 1
        continue
    if time < 0:
        break

print(counter) 
  
