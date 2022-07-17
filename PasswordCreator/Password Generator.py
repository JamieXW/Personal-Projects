#user input for password length
password_length = int(input('How many characters long do you want your password to be?: '))

#user input for uppercase
upper = input('Do you want uppercase letters? (type YES or NO): ')
if upper == "YES": 
    amountupper = int(input('How many uppercase letters would you like? (type 0 if you do not care about the number): '))

#user input for symbols
sym = input('Do you want symbols? (type YES or NO): ')
if sym == "YES": 
    amountsym = int(input('How many symbols would you like? (type 0 if you do not care about the number): '))

#user input for numbers
num = input('Do you want numbers? (type YES or NO): ')
if num == "YES": 
    amountnum = int(input('How many numbers would you like? (type 0 if you do not care about the number): '))

#check if numbers make sense


checkcounter = 0
if upper != "NO":
    checkcounter += amountupper
if sym != "NO":
    checkcounter += amountsym
if num != "NO":
    checkcounter += amountnum
if checkcounter > password_length:
    print('try again') 
    exit()


all = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()'" 
numbers = "1234567890"

arr = []
counter = password_length

import random

if upper == "YES":
    if amountupper == 0:
        all += uppercase
    else:
        for i in range (0, amountupper): 
            x = random.randint(0, len(uppercase) - 1)
            arr.append(uppercase[x])
            counter-=1 
if sym == "YES":
    if amountsym == 0:
        all += symbols
    else:
        for i in range (0, amountsym): 
            x = random.randint(0, len(symbols) - 1)
            arr.append(symbols[x])
            counter-=1 
if num == "YES":
    if amountnum == 0:
        all += numbers
    else:
        for i in range (0, amountnum): 
            x = random.randint(0, len(numbers) - 1)
            arr.append(numbers[x])
            counter-=1 
if counter > 0:
    for i in range (0, counter): 
        x = random.randint(0, len(all) - 1)
        arr.append(all[x])

print(arr) 

import random

new = random.sample(arr, len(arr))
print(new) 

password = ""
for i in range (0, len(new)):
    password += new[i]

print("your password is: " + password) 


