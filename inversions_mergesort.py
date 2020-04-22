import random

def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        m = len(arr) // 2
        L = arr[:m]
        R = arr[m:]
        L, li = mergeSortInversions(L)
        R, ri = mergeSortInversions(R)
        c = []
        i = 0
        j = 0
        inversions = 0 + li + ri
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            c.append(L[i])
            i += 1
        else:
            c.append(R[j])
            j += 1
            inversions += (len(L)-i)
    c += L[i:]
    c += R[j:]
    return c, inversions


t = [random.randint(1,100) for _ in range(30)]
print(t)
sorted, cnt = mergeSortInversions(t)
print(cnt)
print(t)
print(sorted)