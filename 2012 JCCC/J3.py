F = open("C:\\Users\jamie\Downloads\J3\j3.3.in", "r")
factor = int(F.readline())


for i in range (0, factor):
    list = []
    for x in range (0, factor):
        list.append('*') 
    for x in range (0, factor):
        list.append('X')
    for x in range (0, factor):
        list.append('*') 
    print(list) 

for i in range (0, factor):
    list = []
    for x in range (0, factor):
        list.append(' ') 
    for x in range (0, factor):
        list.append('X')
    for x in range (0, factor):
        list.append('X') 
    print(list) 

for i in range (0, factor):
    list = []
    for x in range (0, factor):
        list.append('*') 
    for x in range (0, factor):
        list.append(' ')
    for x in range (0, factor):
        list.append('*') 
    print(list) 

