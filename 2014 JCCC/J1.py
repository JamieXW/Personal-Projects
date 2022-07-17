F = open("C:\\Users\jamie\Downloads\j1\j1.6.in", "r") 
side1 = int(F.readline())
side2 = int(F.readline())
side3 = int(F.readline())

total = side1 + side2 + side3
if side1 == side2 and side2 == side3:
    print("Equalateral")
if total == 180 and side1 == side2 and side1 != side3:
    print("Iscosceles")
if total == 180 and side2 == side3 and side1 != side3:
    print("Iscosceles")
if total == 180 and side1 == side3 and side2 != side3:
    print("Iscosceles")
if total == 180 and side1 != side2 and side3 != side2:
    print("Scalene")
if total != 180:
    print("Error")