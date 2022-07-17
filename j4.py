F = open("C:\\Users\jamie\Downloads\j4\j4\j4.sample.01.in", "r")
T = F.readline()
S = F.readline().strip()

count = 0 
result = False

for count in range(len(S)):
    S = S[1:]+S[0] 
    if S in T:
        result = True
        break

if result == True:
    print("yes") 
else:
    print("no")        





