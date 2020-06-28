def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quicksort(arr, l, r):
    if l < r:
        piv = partition(arr, l, r)
        quicksort(arr, l, piv - 1)
        quicksort(arr, piv + 1, r)

arr = [ 23,42,6,2,54,26,7,7,32,235,67,4,56,52,43,24,675,6,74,6]
quicksort(arr,0,len(arr)-1)
print((arr))