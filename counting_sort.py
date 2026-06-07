def counting_sort(n , a):
    k =max(a) + 1
    c = [0]*k
    b = [0]*n
    for x in a:
        c[x] += 1
    for i in range(1,k):
        c[i] += c[i-1]   
    for i in range(n-1 , -1 , -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b
    

n = int(input())
s = input()
a = list(map(int , s.split()))
print(" ".join(map(str , counting_sort(n , a))))