#input
n = int(input()) 
a = [[0 for i in range (n)] for j in range (n)]
for i in range (n):
     line = input()
     d = line.split()
     d = list(map(int, d)) 
     a[i] = d

#find the smallest number
if (a[0][0] < a[0][n-1]): 
     j = 0
else:
     j = n-1
if (a[0][j] < a[n-1][j]):
     i = 0
else: 
     i = n-1

#top left
if (i == 0 and j ==0):
     for x in range(n):
          for y in range(n):
               print(a[x][y], end='') 
               prunt(' ', end='')
          print('')

#top right
if (i == 0 and j > 0):
     for y in range(n, 0 , -1):
          for x in range(n):
               print(a[x][y-1], end="")
               print(' ', end='')
          print('') 

#bottom right
elif (i > 0 and j > 0):
     for x in range(n, 0, -1):
          for y in range(n, 0, -1):
               print(a[x-1][y-1], end='')
               print(' ', end='')
          print('')

#bottom lef
else: 
     for y in range(n):
          for x in range(n, 0, -1):
               print(a[x-1][y], end='')
               print(' ', end='')
          print('') 
