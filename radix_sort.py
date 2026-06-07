def counting_sort_based_on_digit(n ,a , exp , k):
    c = [0]*k
    b = [0]*n
    for x in a:
        digit = (x // exp) % 10
        c[digit] += 1
    for i in range(1,k):
        c[i] += c[i-1]   
    for i in range(n-1 , -1 , -1):
        digit = (a[i] // exp) % 10
        b[c[digit]-1] = a[i]
        c[digit] -=1
    return b
    
def radix_sort(a , n , d , k):
    exp = 1
    for _ in range(d):
        a = counting_sort_based_on_digit(n , a , exp, k)
        exp*=10
    return a

n = int(input())
a = list(map(int , input().split()))
d = len(str(max(a)))
k = 10
print(" ".join(map(str , radix_sort(a , n , d , k))))