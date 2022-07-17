F = open("C:\\Users\jamie\Downloads\j2\j2.10.in", "r") 
N = int(F.readline())
yesterday = F.readline() 
today = F.readline()

counter = 0 

k = 1
for i in range (0, N, 1):
    if today[k-1:k] == yesterday[k-1:k] and today[k-1:k] == "C":
        counter += 1
        k += 1
    else:
        k += 1

print(counter) 
