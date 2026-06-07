import numpy as np

a = input()
b = input()
n = len(a)
m = len(b)
l = np.zeros((n+1,m+1) , dtype=int)
for i in range(1 , n+1):
    for j in range(1 , m+1):
       if a[i-1] == b[j-1]:
           l[i][j] = l[i-1][j-1] + 1
       else:
           l[i][j] = max(l[i-1][j], l[i][j-1])

print(l[n][m])
