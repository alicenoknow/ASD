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

arr = [10,5,61,6,53,6,44,4,2,76,8,7,42,35,4,3,6]
print(partition(arr,0,len(arr)-1))