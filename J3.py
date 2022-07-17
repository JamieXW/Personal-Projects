f = open("C:\\Users\jamie\Downloads\j3.sample.01.in", "r")
n = f.readline()

X = []
Y = [] 

count = 0
while count < int(n):
    try:
        z = (next(f)).split(',')
        X.append(int(z[0]))
        #print(X)
        Y.append(int(z[1]))
        #print(Y)
        #Y.append(z[1]) 
    except StopIteration as e:
        print(e)
        break
    

xleft = min(X)-1 
yleft = min(Y)-1 
xright = max(X)+1
yright = max(Y)+1 

print(str(xleft)+", "+str(yleft))
print(str(xright)+", "+str(yright)) 
