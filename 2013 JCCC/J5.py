F = open("C:\\Users\jamie\Downloads\J5\j5.1.in", "r") 
team = int(F.readline())
games = int(F.readline())

list = []
for i in range (0, games): 
    line = F.readline()
    line = line.split(' ')
    line[3] = line[3].strip('\n') 
    for x in range (0, 4):
        list.append(line[x]) 

print(list) 

team1score = 0
team2score = 0
team3score = 0
team4score = 0

k = 0
for i in range (0, games):
    if list[k+2] > list[k+3]:
        if list[k] == '1':
            team1score += 3
        elif list[k] == '2':
            team2score += 3
        elif list[k] == '3':
            team3score += 3
        elif list[k] == '4':
            team4score += 3
    if list[k+2] < list[k+3]:
        if list[k+1] == '1':
            team1score += 3
        elif list[k+1] == '2':
            team2score += 3
        elif list[k+1] == '3':
            team3score += 3
        elif list[k+1] == '4':
            team4score += 3
    if list[k+2] == list[k+3]:
        if list[k+1] == '1':
            team1score += 1
        elif list[k+1] == '2':
            team2score += 1
        elif list[k+1] == '3':
            team3score += 1
        elif list[k+1] == '4':
            team4score += 1
        elif list[k] == '1':
            team1score += 1
        elif list[k] == '2':
            team2score += 1
        elif list[k] == '3':
            team3score += 1
        elif list[k] == '4':
            team4score += 1
    k+= 4

print(team1score)
print(team2score)
print(team3score)
print(team4score)