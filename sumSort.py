import random


def partition(B, arr, l, r):
    pivot = arr[l]
    i = l-1
    j = r+1
    while True:
        j -= 1
        i += 1
        while arr[j] > pivot:
            B[j] = arr[j]
            j -= 1
        while arr[i] < pivot:
            B[i] = arr[i]
            i += 1
        if i < j:
            B[i] = arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        else: return j


def select(A, B, k, l, r):
    if l == r:
        B[l] = A[l]
        return
    p = partition(B, A, l, r)
    if p == k:
        B[p] = A[p]
        return
    elif p < k: return select(A, B, p + 1, r, k)
    return select(A, B, l, p-1, k)


def sumSort(A, n):
    B = [None for _ in range(n * n)]
    l = 0
    r = n*n-1
    k = n-1
    while k < n*n:
        select(A, B, k, l, r)
        l = k
        k += n
    return B


n = 5
A = [random.randint(1, 20) for _ in range(n*n)]
print(A)
B = sumSort(A,n)
print(B)