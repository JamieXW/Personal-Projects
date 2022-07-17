F = open("C:\\Users\jamie\Downloads\J1\j1.5.in", "r")
limit = int(F.readline())
carspeed = int(F.readline())

if carspeed <= limit:
    print("Congratulations, you are within the speed limit")
elif carspeed - limit >= 1 and carspeed - limit <= 20:
    print("You are speeding and your fine is $100")
elif carspeed - limit >= 21 and carspeed - limit <= 30:
    print("You are speeding and your fine is $270")
elif carspeed - limit >= 31:
    print("You are speeding and your fine is $500")
