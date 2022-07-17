F = open("C:\\Users\jamie\Downloads\j3\j3.samp1.in", "r") 
word = F.readline() 
print(word) 

counter = 0
for i in range (0, len(word) + 1):
    for s in range (1, len(word)):
        p = word[i:s] 
        print(p)
        if p == p[::-1]:
            length = len(p)
        if length>counter:
            counter = length

print(counter) 


    