P = int(input("Infected Limit: "))
N = int(input("Number of People Infected on Day 0: "))
R = int(input("Number of People 1 Infected infects the next day: "))

days = 0
I = N
Total = I

while Total <= P:
    I = I*R
    Total += I
    days += 1

print(days) 
