F = open("C:\\Users\jamie\Downloads\j3\j3\j3.03.in", "r")
N = int(F.readline())



#for(int i = 1; i <= N; i += 1)
    # str line = read.line()
    #"+++===!!!"
    #line = [+, +, +, =, =, =, !, !, !]
    #c = string[0] = =
    #count = 0
    #for(int k = 0; k < strlen(line); ++k)
        # char temp = line[k]
        # is temp = c?
            # yes: count += 1
            # no: 
                # print ("count c") -> "3 +"
                # count = 1
                # c = temp = line[k] = "="
for i in range(0,N,1):
    line = str(F.readline()) 
    c = str(line[0]) 
    count = 1
    result = ""
    for k in range(1,len(line),1): 
        chartemp = line[k] 
        if chartemp == c:
            count += 1
        else:  
            sent = (str(count) + " " + str(c))
            result = result + " " + sent
            count = 1 
            c = line[k]
    print(result) 
        
     