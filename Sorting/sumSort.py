import random

# O ( n^2 )

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

#=================================================================================

# O( n^2 ) i n pamieci

class Nth:
    def __init__(self):
        self.sum = 0
        self.table = []

def SumSort(A, B, n):
    C = [None for _ in range(n)]
    j = 0
    idx = 0
    sum = 0
    for i in range(n*n):
        if j == n:
            C[idx] = Nth()
            C[idx].sum = sum
            C[idx].table = A[i-n:i]
            j = 0
            sum = 0
            idx += 1
        j += 1
        sum += A[i]

    C[idx] = Nth()
    C[idx].sum = sum
    C[idx].table = A[i - n:i]

    quicksort(C, 0, n-1)
    for i in range(n):
        B.extend(C[i].table)
        print(C[i].sum, end=" ")
    print(B)


def partition2(arr, l, r):
    i = l - 1
    pivot = arr[r].sum
    for j in range(l, r):

        if arr[j].sum <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quicksort(arr, l, r):
    if l < r:
        piv = partition2(arr, l, r)
        quicksort(arr, l, piv - 1)
        quicksort(arr, piv + 1, r)

#=================================================================================
n = 5
A = [random.randint(1, 20) for _ in range(n*n)]
print(A)
SumSort(A, [], n)
B = sumSort(A,n)
print(B)


