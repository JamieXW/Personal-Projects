F = open("C:\\Users\jamie\Downloads\j1\j1\j1.sample.02.in", "r")
N = int(F.readline()) 

P = 5 * N - 400
print(P)

if N == 100:
    print("0") 
elif N > 100:
    print("-1") 
else:
    print("1") 
