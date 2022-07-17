F = open("C:\\Users\jamie\Downloads\j3\j3.5.in", "r") 
Rounds = int(F.readline()) 

Antonia = 100
David = 100

for i in range (0, Rounds):
    rolls = F.readline() 
    rolls = rolls.split(' ') 
    rolls[1] = rolls[1].strip('\n') 
    if rolls[0] < rolls[1]:
        Antonia = Antonia - int(rolls[1])
    if rolls[1] < rolls[0]:
        David = David - int(rolls[0])
    if rolls[0] == rolls[1]:
        continue


print(Antonia)
print(David) 
