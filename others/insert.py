a = []
import random

def insertSorted(v, num):
    v.append(num)
    if len(v) == 1:
        return
    else:
        i = len(v) - 1
        aux = v[-1]
        j = i - 1
        while j>=0 and v[j] > aux:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = aux

for i in range (10):
    x = random.randint(0,100)
    insertSorted(a, x)
print(a)    
