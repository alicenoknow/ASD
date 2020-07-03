def max_len(A):
    d = 0
    for i in range(len(A)):
        d = max(d, len(A[i]))
    return d


def counting_sort(arr, pos):
    n = len(arr)
    output = [0 for _ in range(n)]
    count = [0 for _ in range(26)]
    for i in range(0, n):
        index = ord(arr[i][pos]) - 97
        count[index] += 1

    for i in range(1, 26):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(arr[i][pos]) - 97
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort_strings(A, M):
    for i in range(M):
        counting_sort(A, i)


def bucket_sort(A):
    M = max_len(A)
    buckets = [[] for _ in range(M+1)]
    for i in range(len(A)):
        buckets[len(A[i])].append(A[i])
    for i in range(M+1):
        radix_sort_strings(buckets[i], i)
    R = []
    for i in range(M+1):
        R += buckets[i]
    print(R)


A = ["ala", "lol", "rrr", "a","daojasiod", "asda", "t", "l", "oasaaad", "aa", "gkf", "aoa", "zzz", "sds"]
bucket_sort(A)

