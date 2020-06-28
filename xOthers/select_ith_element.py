def partition(arr, l, r):
    pivot = arr[l]
    i = l-1
    j = r+1
    while True:
        j -= 1
        i += 1
        while arr[j] > pivot :  j -= 1
        while arr[i] < pivot :  i += 1
        if i<j: arr[i], arr[j] = arr[j], arr[i]
        else: return j

def select(arr, l, r, i):
    if l == r: return arr[l]
    p = partition(arr,l,r)
    if p == i: return arr[p]
    elif p < i: return select(arr, p+1, r, i)
    return select(arr, l, p-1, i)


arr = [2,5,4,8,6,9,1,3,7]
print(select(arr,0,8,4))
print(arr)