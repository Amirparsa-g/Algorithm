
def swap(arr , i , j):
    arr[i] , arr[j] = arr[j] , arr[i]

def partition(a, pivot):
    n = len(a)
    pivot_index = a.index(pivot)
    swap(a, pivot_index, n-1)
    i = -1
    for j in range(n-1):
        if a[j] < pivot:
            i += 1
            swap(a, i, j)
    swap(a, i+1, n-1)
    return i+1

def selection(a,k):
    medians=[]
    n = len(a)
    if n <= 5:
        a = sorted(a)
        return a[k]
    
    for i in range(0 , n , 5):
        group = sorted(a[i:i+5])
        mid = len(group)//2
        medians.append(group[mid])
    pivot = selection(medians , len(medians)//2)
    q = partition(a , pivot)
    if k == q:
        return a[q]
    elif k < q:
        return selection(a[:q-1] , k)
    elif k > q:
        return selection(a[q+1:] , k-q-1)
    
