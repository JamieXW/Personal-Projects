F = open("C:\\Users\jamie\Downloads\J2\j2.1-1.in", "r") 
word = F.readline()
list = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']


print(word)
mark = "YES"
for i in range (0, len(word)-1):
    if list.count(word[i]) == 1:
        continue
    else: 
        mark = "NO"
        break

print(mark) 
