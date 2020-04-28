def reverse(arr, l, r):
    while l < r and l >= 0 and r < len(arr):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


def move_values(arr, k):
    piv = len(arr) - (k % len(arr))
    reverse(arr, 0, piv-1)
    reverse(arr, piv, len(arr)-1)
    reverse(arr, 0, len(arr)-1)


arr = [12, 9, 4, 52, 5, 11, 7, 55, 6, 54, 3, 2, 14, 5]
move_values(arr, 6)
print(arr)