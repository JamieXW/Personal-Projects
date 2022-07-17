F = open("C:\\Users\jamie\Downloads\j4\j4\j4.09.in", "r")
Q = F.readlines()
Q = Q[0].strip('\n') 
numberofLs = Q.count("L")
numberofMs = Q.count("M") 

Largesection = Q[0:numberofLs]
Mediumsection = Q[numberofLs:(numberofLs + numberofMs)] 

nonLsinLarge = numberofLs - int(Largesection.count("L"))
nonMsinMedium = numberofMs - int(Mediumsection.count("M"))

LsinMedium = Mediumsection.count("L")
MsinLarge = Largesection.count("M")
 
sum = nonLsinLarge + nonMsinMedium - min(LsinMedium, MsinLarge) 
print(sum) 