F = open("C:\\Users\jamie\Downloads\j2\j2.1.in", "r")
line = F.readline()
print(line) 


print(line)
happys = line.count(":-)")
sads = line.count(":-(")


if happys == 0 and sads == 0:
    print("none")
elif happys == sads:
    print("unsure") 
elif happys > sads:
    print("happy")
else:
    print("sad") 