def merge(l , r):
    i = 0
    j = 0
    count=0
    result=[]
    l.append(float('inf'))
    r.append(float('inf'))
    while len(result) < len(l) + len(r) -2:
        if l[i] >= r[j]:
            result.append(r[j])
            j +=1
        elif l[i] <= r[j]:
            result.append(l[i])
            i += 1
     
    return result


def merge_sort(a):
    n = len(a)
    if n<= 1:
        return a
    
    q = n // 2
    l=a[:q]
    r=a[q:]
    sorted_left = merge_sort(l)
    sorted_right= merge_sort(r)
    return merge(sorted_left, sorted_right)

s = input("enter an unsorted array:\n")
arr = list(map(int,s.split()))
print(merge_sort(arr))