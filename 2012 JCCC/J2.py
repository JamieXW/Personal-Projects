F = open("C:\\Users\jamie\Downloads\J2\j2.3.in", "r")
r1 = int(F.readline())
r2 = int(F.readline())
r3 = int(F.readline())
r4 = int(F.readline())

if r1 == r2 and r2 == r3 and r3 == r4:
    print('Fish at constant depth')
elif r2 > r1 and r3 > r2 and r4 > r3:
    print("Fish rising")
elif r2 < r1 and r3 < r2 and r4 < r3:
    print("Fish diving")
else: 
    print("No fish") 

