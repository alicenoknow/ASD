def countingSort(A,n,exp):
    n = len(A)
    B = [0] * n
    C = [0] * n
    for i in range(n):
         index = A[i] // exp
         C[index % n] += 1
    for i in range(1, n):
         C[i] += C[i-1]
    for i in range(n-1,-1,-1):
         index = A[i] // exp
         C[index % n] -= 1
         B[C[index % n]] = A[i]
    for i in range(n):
         A[i] = B[i]
def RadixSort(arr,n):
     countingSort(arr,n,1)
     countingSort(arr,n,n)


spam = [24, 2, 5, 10, 4]
RadixSort(spam, 5)
print(spam)