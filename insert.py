a = [1,2]

def insertSorted(a, num):
    n = len(a)
    i = n-1
    while i >= 0 and a[i] > num:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = num
insertSorted(a,3)
print(a)    
