F = open("C:\\Users\jamie\Downloads\j1\j1.7.in", "r")
first = int(F.readline())
second = int(F.readline())
third = int(F.readline())
fourth = int(F.readline()) 

print(first, second, third, fourth) 

if first == 8 or 9:
    call = "ignore" 
else: 
    call = "answer"  


if call == "ignore" and second == third:
    call = "ignore" 
else: 
    call = "answer" 

if call == "ignore" and (fourth == 8 or 9):
    call = "ignore" 
else: 
    call = "answer" 
    
print(call) 