
def factorial(x):

    res = 1
    for i in range(2,x+1):
        res *= i
    return res

def qsort(arr, l=0, r=None):
    if r is None: r = len(arr) - 1
    i, j = l, r
    pivot = arr[(l + r) / 2]
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1; j -= 1
    if l < j: qsort(arr, l, j)
    if r > i: qsort(arr, i, r)

t = [random.randint(1,100) for _ in range(30)]