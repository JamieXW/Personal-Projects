F = open("C:\\Users\jamie\Downloads\j3\j3.1.in", "r")
line = F.readline()
print(line)

newletter = ""
cons = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
vowel = ["a","e","i","o","u"] 

for i in range (0, len(line)-1):
  
    letter = str(line[i])
# part 1 is correct
    for c in range (0, 25):
        if letter == cons[c]:
            newletter = newletter+(letter)
           
#part 2 does not add anything
            for v in range (1,25):
                if cons[c-v] == vowel[0]  or cons[c-v] == vowel[1] or cons[c-v] == vowel[2] or cons[c-v] == vowel[3] or cons[c-v] == vowel[4]:
                    newletter = newletter+(cons[c-v])
                    print(cons[c-v]) 
                    break
                elif cons[c+v] == vowel[0]  or cons[c+v] == vowel[1] or cons[c+v] == vowel[2] or cons[c+v] == vowel[3] or cons[c+v] == vowel[4]:
                    newletter = newletter+(cons[c+v])
                    print(cons[c+v]) 
                    break
# does not add anything
                for v in range (0,4):
                    if cons[c+1] == vowel[v]:
                        
                        continue 
# this is what is adding the random letters
                    else:
                        newletter = newletter+(cons[c+1])
                       
                        
                        break
                    

print(newletter) 


           

