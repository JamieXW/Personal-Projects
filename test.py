t = int(input())
arr = []
for i in range (0, t):
    n = int(input())
    arr.append(n)
arr.sort()
for x in range (0, t):
    print(arr[x])
