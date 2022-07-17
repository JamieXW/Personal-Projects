D
distances = F.readline()
distances = distances.split(' ') 
distances[3] = distances[3].strip('\n') 
D = distances


print(0, int(D[0]),int(D[0]) + int(D[1]),int(D[0]) + int(D[1]) + int(D[2]),int(D[0]) + int(D[1]) + int(D[2]) + int(D[3])) 
print(int(D[0]), 0, int(D[1]), int(D[1]) + int(D[2]), int(D[1]) + int(D[2]) + int(D[3])) 
print(int(D[0]) + int(D[1]), int(D[1]), 0, int(D[2]), int(D[2]) + int(D[3]))
print(int(D[0]) + int(D[1]) + int(D[2]), int(D[1]) + int(D[2]), int(D[2]), 0, int(D[3])) 
print(int(D[0]) + int(D[1]) + int(D[2]) + int(D[3]), int(D[1]) + int(D[2]) + int(D[3]), int(D[2]) + int(D[3]), + int(D[3]), 0)