F = open("C:\\Users\jamie\Downloads\j1\j1.9.in", "r")
month = int(F.readline())
day = int(F.readline()) 

print(month, day) 

status = "" 
if month < 2:
    status = "before"
elif month == 2:
    status = "special"
elif month > 2:
    status = "after" 

if status == "special":
    if day < 18:
        status = "before"
    elif day == 18:
        status = "special"
    elif day > 18:
        status = "after" 

print(status) 