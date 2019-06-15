a = [
    [1,2,3],
    [5,6,7]
]

def deepcopy(arr):
    b = []
    for line in arr:
        l = []
        for col in line:
            l.append(col)
        b.append(l)
    return b

b = deepcopy(a)
a[0][0] = 10
a[1][1] = 1000
print(a)
print(b)