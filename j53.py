F = open("C:\\Users\jamie\Downloads\j5\j5\j5.sample.02.in", "r") 
M = int(F.readline()); N = int(F.readline()); length = int(F.readline()) 

list = []

for i in range (0, length, 1):
    item = str(F.readline())
    list.append(item) 

list = sorted(list, key=str.lower)
print(list) 
k = 1
while i < len(list): 
    if list[k] == list[k-1]:
        list.remove(list[k]) 
        list.remove(list[k-1]) 
    else:
        continue
    k += 1
k = 1
print(list) 